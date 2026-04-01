# -*- coding: utf-8 -*-
"""
游戏王查卡核心功能模块
不依赖asrtbot，可独立使用

免责声明：
- 卡片数据来源：https://github.com/moecube/ygopro-database
- 卡片图片来源：https://cdn.233.momobako.com/ygopro/pics/
- 本模块仅用于学习和娱乐目的，不用于商业用途
- 所有卡片数据和图片的版权归其各自的所有者所有
- 游戏王（Yu-Gi-Oh!）及其相关内容为 KONAMI 公司的注册商标
- 本模块为非官方工具，与 KONAMI 公司无任何关联
"""

import os
import sqlite3
import subprocess
import time
import threading
import asyncio
from typing import Dict, Any, List


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
        self.data_dir = data_dir if data_dir else os.getcwd()
        self.db_dir = os.path.join(self.data_dir, "ygopro-database")
        
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
            stderr=asyncio.subprocess.STDOUT,
        )
        
        stdout_lines = []
        current_line = []
        
        logger.info(f"开始实时读取 {description} 输出...")
        
        while True:
            char = await process.stdout.read(1)
            if not char:
                try:
                    returncode = await asyncio.wait_for(process.wait(), timeout=1)
                    break
                except asyncio.TimeoutError:
                    continue
            
            try:
                decoded_char = char.decode('utf-8', errors='replace')
            except:
                decoded_char = str(char)
            
            if decoded_char == '\r' or decoded_char == '\n':
                if current_line:
                    line = ''.join(current_line)
                    logger.info(f"[{description}] {line}")
                    stdout_lines.append(line + '\n')
                    current_line = []
            else:
                current_line.append(decoded_char)
        
        if current_line:
            line = ''.join(current_line)
            logger.info(f"[{description}] {line}")
            stdout_lines.append(line + '\n')
        
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
            
            if os.path.exists(self.db_dir):
                logger.info("数据库目录已存在，执行git pull更新")
                result = await self._execute_git_command(
                    ["git", "pull"],
                    cwd=self.db_dir,
                    description="git pull"
                )
            else:
                logger.info("数据库目录不存在，开始克隆数据库")
                logger.info(f"克隆目标目录: {self.data_dir}")
                logger.info("正在执行 git clone，这可能需要一些时间...")
                
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
        """处理卡片查询"""
        logger.info("开始查询，执行SQL查询...")
        
        cdb_path = os.path.join(self.db_dir, "locales", "zh-CN", "cards.cdb")
        
        if not os.path.exists(cdb_path):
            cdb_path = os.path.join(self.db_dir, "cards.cdb")
        
        results = []
        
        if not os.path.exists(cdb_path):
            logger.error(f"数据库文件不存在: {cdb_path}")
            logger.error(f"数据目录: {self.data_dir}")
            logger.error(f"数据库目录: {self.db_dir}")
            logger.error(f"完整路径: {cdb_path}")
            raise Exception(f"数据库文件不存在: {cdb_path}\n请先使用命令 `/更新卡片数据库` 或 `/update_database` 下载数据库")
        
        try:
            conn = sqlite3.connect(cdb_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if not sql:
                sql = """
                    SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc, d.ot
                    FROM datas d 
                    JOIN texts t ON d.id = t.id
                """
            
            logger.info(f"执行SQL: {sql}")
            cursor.execute(sql)
            query_results = cursor.fetchall()
            
            attribute_map = {
                0: "无",
                1: "地",
                2: "水",
                4: "炎",
                8: "风",
                16: "光",
                32: "暗"
            }
            
            race_map = {
                0: "无",
                1: "战士",
                2: "魔法师",
                4: "天使",
                8: "恶魔",
                16: "不死",
                32: "机械",
                64: "水",
                128: "炎",
                256: "岩石",
                512: "鸟兽",
                1024: "植物",
                2048: "昆虫",
                4096: "雷",
                8192: "龙",
                16384: "兽",
                32768: "兽战士",
                65536: "恐龙",
                131072: "鱼",
                262144: "海龙",
                524288: "爬虫",
                1048576: "念动力",
                2097152: "幻神兽",
                4194304: "创造神",
                8388608: "幻龙"
            }
            
            ocg_tcg_map = {
                1: "OCG",
                2: "TCG",
                3: "OCG|TCG",
                4: "自定义",
                9: "OCG|TCG",
                11: "OCG|TCG"
            }
            
            for row in query_results:
                row_dict = dict(row)
                
                if 'id' not in row_dict:
                    continue
                
                card_id = row_dict.get('id')
                has_full_fields = all(key in row_dict for key in ['name', 'type', 'attribute', 'level', 'race', 'atk', 'def', 'desc', 'ot'])
                
                if not has_full_fields:
                    try:
                        full_query = f"""
                            SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc, d.ot
                            FROM datas d 
                            JOIN texts t ON d.id = t.id
                            WHERE d.id = ?
                        """
                        cursor.execute(full_query, (card_id,))
                        full_row = cursor.fetchone()
                        if full_row:
                            row_dict = dict(full_row)
                        else:
                            if 'name' not in row_dict or row_dict.get('name') is None:
                                continue
                    except Exception as e:
                        logger.error(f"查询完整卡片信息失败: {e}")
                        if 'name' not in row_dict or row_dict.get('name') is None:
                            continue
                
                card_id = row_dict.get('id')
                name = row_dict.get('name', '')
                card_type = row_dict.get('type', 0)
                attribute = row_dict.get('attribute', 0)
                level = row_dict.get('level', 0)
                race = row_dict.get('race', 0)
                atk = row_dict.get('atk', 0)
                defense = row_dict.get('def', 0)
                desc = row_dict.get('desc', '')
                ot = row_dict.get('ot', 3)
                
                card_type_str = "怪兽"
                ocg_tcg_str = ocg_tcg_map.get(ot, "未知")
                is_tuner = (card_type & 16384) != 0
                subtypes = []
                
                if card_type & 2:
                    if card_type & 0x80:
                        subtypes.append("仪式")
                    elif card_type & 0x10000:
                        subtypes.append("速攻")
                    elif card_type & 0x20000:
                        subtypes.append("永续")
                    elif card_type & 0x40000:
                        subtypes.append("装备")
                    elif card_type & 0x80000:
                        subtypes.append("场地")
                    else:
                        subtypes.append("通常")
                    card_type_str = "|".join(subtypes) + "|魔法"

                elif card_type & 4:
                    if card_type & 0x100000:
                        subtypes.append("反击")
                    elif card_type & 0x20000:
                        subtypes.append("永续")
                    else:
                        subtypes.append("通常")
                    card_type_str = "|".join(subtypes) + "|陷阱"

                elif card_type & 1:
                    if card_type & 0x4000000:
                        subtypes.append("连接")
                    elif card_type & 0x800000:
                        subtypes.append("XYZ")
                    elif card_type & 8192:
                        subtypes.append("同调")
                    elif card_type & 64:
                        subtypes.append("融合")

                    if card_type & 0x1000000:
                        subtypes.append("灵摆")

                    if card_type & 32:
                        subtypes.append("效果")
                    elif not (card_type & 64) and not (card_type & 8192) and not (card_type & 0x800000) and not (card_type & 0x4000000):
                        subtypes.append("通常")

                    card_type_str = "|".join(subtypes) + "|怪兽"
                
                attribute_str = attribute_map.get(attribute, "无")
                race_str = race_map.get(race, "未知")

                card_info_base = {
                    "id": card_id,
                    "name": name,
                    "type": card_type_str,
                    "ocg_tcg": ocg_tcg_str,
                    "attribute": attribute_str,
                    "race": race_str,
                    "attack": atk,
                    "description": desc,
                }
                
                if is_tuner:
                    card_info_base["tuner"] = True
                
                is_link_monster = (card_type & 0x4000000) != 0
                is_xyz_monster = (card_type & 0x800000) != 0
                
                if not is_xyz_monster and not is_link_monster:
                    card_info_base["level"] = level
                
                if not is_link_monster:
                    card_info_base["defense"] = defense
                
                if is_xyz_monster:
                    card_info_base["rank"] = level
                
                if is_link_monster:
                    card_info_base["link"] = level
                
                card = card_info_base
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
        image_url = f"https://cdn.233.momobako.com/ygopro/pics/{card_id}.jpg"
        logger.info(f"生成卡片图片链接: {card_id}")
        return image_url
