# -*- coding: utf-8 -*-
"""
游戏王查卡核心功能模块
不依赖asrtbot，可独立使用
"""

import os
import sqlite3
import subprocess
import time
import threading
import asyncio
from typing import Dict, Any, List

# 模拟 logger 接口
class Logger:
    def info(self, msg):
        print(f"[INFO] {msg}")
    
    def error(self, msg):
        print(f"[ERROR] {msg}")
    
    def warning(self, msg):
        print(f"[WARNING] {msg}")

logger = Logger()

class CardQueryCore:
    """游戏王查卡核心功能"""
    
    def __init__(self, data_dir=None):
        """初始化核心功能"""
        # 设置数据目录
        self.data_dir = data_dir if data_dir else os.getcwd()
        
        # 数据库目录路径 - 使用 os.path.join 确保跨平台兼容
        self.db_dir = os.path.join(self.data_dir, "ygopro-database")
        
        # 记录路径信息以便调试
        logger.info(f"CardQuery 数据目录: {self.data_dir}")
        logger.info(f"数据库目录: {self.db_dir}")
        logger.info(f"操作系统: {os.name}")
        logger.info(f"路径分隔符: {os.sep}")
    
    async def _execute_git_command(self, cmd, cwd, description):
        """执行 git 命令并实时输出日志"""
        logger.info(f"开始执行 {description}...")
        logger.info(f"命令: {' '.join(cmd)}")
        logger.info(f"工作目录: {cwd}")
        
        process = await asyncio.create_subprocess_exec(
            *cmd,
            cwd=cwd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,  # 将 stderr 重定向到 stdout
        )
        
        stdout_lines = []
        current_line = []
        
        logger.info(f"开始实时读取 {description} 输出...")
        
        # 实时读取输出 - 逐字符读取以处理 \r 进度更新
        while True:
            char = await process.stdout.read(1)
            if not char:
                if process.returncode is not None:
                    break
                continue
            
            try:
                decoded_char = char.decode('utf-8', errors='replace')
            except:
                decoded_char = str(char)
            
            if decoded_char == '\r' or decoded_char == '\n':
                # 行结束，输出当前行
                if current_line:
                    line = ''.join(current_line)
                    logger.info(f"[{description}] {line}")
                    stdout_lines.append(line + '\n')
                    current_line = []
            else:
                current_line.append(decoded_char)
        
        # 处理剩余的数据
        if current_line:
            line = ''.join(current_line)
            logger.info(f"[{description}] {line}")
            stdout_lines.append(line + '\n')
        
        await process.wait()
        logger.info(f"{description} 返回码: {process.returncode}")
        
        if process.returncode != 0:
            error_output = ''.join(stdout_lines)
            logger.error(f"{description} 失败，返回码: {process.returncode}")
            logger.error(f"错误输出: {error_output}")
            raise Exception(f"{description} 失败，返回码: {process.returncode}\n错误输出: {error_output}")
        
        return type('Result', (), {
            'stdout': ''.join(stdout_lines),
            'stderr': ''
        })()
    
    async def update_database(self) -> Dict[str, Any]:
        """更新游戏王数据库"""
        try:
            logger.info("开始更新游戏王数据库...")
            logger.info(f"数据目录: {self.data_dir}")
            logger.info(f"数据库目录: {self.db_dir}")
            
            # 进入ygopro-database目录并执行git pull
            if os.path.exists(self.db_dir):
                logger.info("数据库目录已存在，执行git pull更新")
                # 执行git pull更新数据库
                result = await self._execute_git_command(
                    ["git", "pull"],
                    cwd=self.db_dir,
                    description="git pull"
                )
            else:
                logger.info("数据库目录不存在，开始克隆数据库")
                logger.info(f"克隆目标目录: {self.data_dir}")
                logger.info("正在执行 git clone，这可能需要一些时间...")
                
                # 首次克隆数据库
                # 直接使用 GitHub 原始地址
                result = await self._execute_git_command(
                    ["git", "clone", "--progress", "https://github.com/moecube/ygopro-database.git", "ygopro-database"],
                    cwd=self.data_dir,
                    description="git clone"
                )
                
                logger.info("git clone执行完成")
            
            logger.info("数据库更新完成")
            
            return {
                "status": "success",
                "message": "数据库更新成功",
                "output": result.stdout,
                "error": result.stderr if hasattr(result, 'stderr') else "",
                "card_count": 0
            }
        except Exception as e:
            logger.error(f"更新数据库失败: {e}")
            import traceback
            traceback.print_exc()
            return {
                "status": "error",
                "message": f"更新数据库失败: {str(e)}"
            }
    

    
    def query_card(self, sql: str = "") -> Dict[str, Any]:
        """处理卡片查询
        
        参数:
            sql: SQL查询语句
        
        数据库结构描述：
        - datas表：存储卡片基本信息
          id: 卡片ID
          type: 卡片类型（1=怪兽, 2=魔法, 4=陷阱）
          attribute: 属性（0=无, 1=地, 2=水, 4=炎, 8=风, 16=光, 32=暗）
          level: 等级
          race: 种族
          atk: 攻击力
          def: 防御力
        
        - texts表：存储卡片文本信息
          id: 卡片ID
          name: 卡片名称
          desc: 卡片描述
        
        表关系：datas.id = texts.id
        """
        # 每次查询时直接执行SQL查询
        logger.info("开始查询，执行SQL查询...")
        
        # 尝试从SQLite数据库直接查询
        cdb_path = os.path.join(self.db_dir, "locales", "zh-CN", "cards.cdb")
        results = []
        
        if not os.path.exists(cdb_path):
            # 数据库文件不存在，先打印路径信息，然后抛出异常
            logger.error(f"数据库文件不存在: {cdb_path}")
            logger.error(f"数据目录: {self.data_dir}")
            logger.error(f"数据库目录: {self.db_dir}")
            logger.error(f"完整路径: {cdb_path}")
            raise Exception(f"数据库文件不存在: {cdb_path}\n请先使用命令 `/更新卡片数据库` 或 `/update_database` 下载数据库")
        
        try:
            conn = sqlite3.connect(cdb_path)
            cursor = conn.cursor()
            
            # 执行传入的SQL查询
            if not sql:
                # 默认查询
                sql = """
                    SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
                    FROM datas d 
                    JOIN texts t ON d.id = t.id
                """
            
            logger.info(f"执行SQL: {sql}")
            cursor.execute(sql)
            query_results = cursor.fetchall()
            
            # 处理查询结果
            attribute_map = {
                0: "无",
                1: "地",
                2: "水",
                4: "炎",
                8: "风",
                16: "光",
                32: "暗"
            }
            
            for row in query_results:
                card_id, name, card_type, attribute, level, race, atk, defense, desc = row
                
                # 解析卡片类型
                card_type_str = "怪兽"
                if card_type & 2:
                    card_type_str = "魔法"
                elif card_type & 4:
                    card_type_str = "陷阱"
                
                # 解析属性
                attribute_str = attribute_map.get(attribute, "无")
                
                # 根据卡片类型确定等级/阶级/链接数
                level_info = {}
                if card_type & 64:  # XYZ怪兽（超量）
                    level_info["rank"] = level
                elif card_type & 128:  # 连接怪兽
                    level_info["link"] = level
                else:  # 其他怪兽
                    level_info["level"] = level
                
                card = {
                    "id": card_id,
                    "name": name,
                    "type": card_type_str,
                    "attribute": attribute_str,
                    "race": race,
                    "attack": atk,
                    "defense": defense,
                    "description": desc,
                    **level_info
                }
                results.append(card)
            
            conn.close()
            logger.info(f"SQL查询完成，找到 {len(results)} 张卡片")
        except Exception as e:
            logger.error(f"SQL查询失败: {e}")
            raise
        
        return {
            "status": "success",
            "query": sql,
            "results": results,
            "count": len(results),
            "note": "正在更新数据库，请稍后查询" if len(results) == 0 else ""
        }
    
    def get_card_image_url(self, card_id: int) -> str:
        """获取卡片图片URL"""
        # 卡片图片URL
        image_url = f"https://cdn.233.momobako.com/ygopro/pics/{card_id}.jpg"
        logger.info(f"生成卡片图片链接: {card_id}")
        return image_url
