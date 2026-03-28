# -*- coding: utf-8 -*-
"""
游戏王查卡插件 - 基于asrtbot
"""

from .card_query_core import CardQueryCore
from astrbot.api.star import Star, register, StarTools
from astrbot.api.event import filter
from astrbot.core.config.astrbot_config import AstrBotConfig
from astrbot.core.platform.astr_message_event import AstrMessageEvent
import astrbot.api.message_components as Comp
from astrbot.api.all import logger
from typing import Dict, Any

@register("astrbot_plugin_ygo_card_query", "Wen", "游戏王查卡插件", "1.0.0")
class CardQueryPlugin(Star):
    def __init__(self, context=None, config: AstrBotConfig = None):
        super().__init__(context, config)
        self.name = "astrbot_plugin_ygo_card_query"
        self.description = "游戏王查卡插件"
        self.version = "1.0.0"
        
        # 获取数据目录
        try:
            data_dir = StarTools.get_data_dir()
        except Exception as e:
            logger.warning(f"StarTools.get_data_dir() 自动获取失败 ({e})，使用手动路径兜底。")
            data_dir = None
        
        # 初始化核心功能
        self.core = CardQueryCore(data_dir)
        
        logger.info("CardQuery 插件初始化完成")
    
    async def terminate(self):
        """插件卸载/关闭时的清理工作"""
        # 这里可以添加清理代码，例如关闭数据库连接等
        logger.info("CardQuery 插件已卸载")
    
    async def _send_text_message(self, event: AstrMessageEvent, message: str):
        """发送文本消息"""
        logger.info("发送查询结果文本")
        await event.send(event.plain_result(message))
    
    async def _handle_query_result(self, event: AstrMessageEvent, result: Dict[str, Any], is_tool_call: bool = False):
        """处理查询结果并发送响应"""
        # 处理查询失败的情况
        if result["status"] != "success":
            error_message = result.get('message', '未知错误')
            logger.error(f"查询出错: {error_message}")
            await self._send_text_message(event, f"❌ 查询出错: {error_message}")
            return f"查询出错: {error_message}"
        
        # 处理无结果的情况
        if result["count"] == 0:
            logger.info("未找到与查询条件相关的卡片")
            no_result_message = "⚠️ 未找到与查询条件相关的卡片"
            await self._send_text_message(event, no_result_message)
            return no_result_message
        
        # 处理有结果的情况
        if result["count"] == 1:
            # 只有一张卡片，发送卡片信息和图片
            first_card = result["results"][0]
            logger.info(f"返回第一张卡片: {first_card['name']}")
            
            # 构建回复消息
            response = f"🔍 查询结果: {first_card['name']}\n"
            response += f"类型: {first_card['type']}\n"
            if "attribute" in first_card:
                response += f"属性: {first_card['attribute']}\n"
            if "attack" in first_card:
                response += f"攻击力: {first_card['attack']}\n"
            if "defense" in first_card:
                response += f"防御力: {first_card['defense']}\n"
            if "level" in first_card:
                response += f"等级: {first_card['level']}\n"
            if "description" in first_card:
                response += f"效果: {first_card['description']}\n"
            
            if result.get("note"):
                response += f"\n💡 {result['note']}"
            
            # 尝试发送图片和文本
            card_id = first_card.get("id")
            if card_id:
                image_url = self.core.get_card_image_url(card_id)
                if image_url:
                    try:
                        chain = []
                        chain.append(Comp.Image.fromURL(image_url))
                        chain.append(Comp.Plain(response))
                        logger.info(f"发送卡片图片和文本: {first_card['name']}")
                        await event.send(event.chain_result(chain))
                    except Exception as e:
                        logger.error(f"发送图片失败: {e}")
                        await self._send_text_message(event, response)
                else:
                    await self._send_text_message(event, response)
            else:
                await self._send_text_message(event, response)
        
        # 处理工具调用的返回信息
        if is_tool_call:
            if result["count"] == 1:
                return "查询完成"
            else:
                # 有多张卡片，返回前三张卡片名称
                top_cards = result["results"][:3]
                card_names = [card["name"] for card in top_cards]
                extra_info = f"查询到多张卡片，前三张是：{', '.join(card_names)}"
                if result["count"] > 3:
                    extra_info += f" 共找到 {result['count']} 张卡片。请提供更多条件以缩小查询范围。"
                else:
                    extra_info += "。请提供更多条件以缩小查询范围。"
                return extra_info
        else:
            return "查询完成"
    
    @filter.llm_tool(name="query_card")
    async def query_card(self, event: AstrMessageEvent, sql: str = ""):
        """查询游戏王卡片信息。

        Args:
            sql(string): SQL查询语句，必须包含 id, name, type, attribute, level, race, atk, def, desc 字段
        
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
        
        示例SQL查询：
        1. 查询青眼白龙：
           SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
           FROM datas d 
           JOIN texts t ON d.id = t.id
           WHERE t.name LIKE '%青眼白龙%'
        
        2. 查询攻击力大于2000的怪兽：
           SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
           FROM datas d 
           JOIN texts t ON d.id = t.id
           WHERE d.type & 1 AND d.atk > 2000
        """
        logger.info(f"开始处理工具调用: query_card, 参数: sql={sql}")
        
        try:
            result = self.core.query_card(sql)
            logger.info(f"查询结果: status={result['status']}, count={result['count']}")
            return await self._handle_query_result(event, result, is_tool_call=True)
        except Exception as e:
            error_message = str(e)
            logger.error(f"查询出错: {error_message}")
            await event.send(event.plain_result(f"❌ 查询出错: {error_message}"))
            return "查询完成"
    
    @filter.command("查卡", alias={"/查卡"})
    async def handle_cha_ka(self, event: AstrMessageEvent):
        """查卡（只查询卡片名称）"""
        message_text = event.get_message_str().strip()
        logger.info(f"收到查卡命令: {message_text}")
        
        parts = message_text.split() if message_text else []

        if len(parts) <= 1:
            logger.info("查卡命令缺少参数")
            await event.send(event.plain_result("请输入要查询的卡片名称，例如: /查卡 青眼白龙"))
            return

        query = " ".join(parts[1:])
        logger.info(f"开始查询卡片: {query}")
        
        # 只查询卡片名称的SQL
        sql = f"""
            SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
            FROM datas d 
            JOIN texts t ON d.id = t.id
            WHERE t.name LIKE '%{query}%'
        """
        
        try:
            result = self.core.query_card(sql)
            logger.info(f"查询结果: status={result['status']}, count={result['count']}")
            await self._handle_query_result(event, result)
        except Exception as e:
            error_message = str(e)
            logger.error(f"查询出错: {error_message}")
            await event.send(event.plain_result(f"❌ 查询出错: {error_message}"))
    
    @filter.command("更新卡片数据库", alias={"/更新卡片数据库"})
    async def handle_update_database(self, event: AstrMessageEvent):
        """手动更新游戏王卡片数据库"""
        logger.info("收到更新卡片数据库命令")
        await event.send(event.plain_result("🔍 正在更新游戏王卡片数据库，请稍候..."))
        
        logger.info("开始执行数据库更新")
        result = await self.core.update_database()
        logger.info(f"数据库更新完成: status={result['status']}")
        
        if result["status"] == "success":
            logger.info(f"数据库更新成功，卡片数量: {result['card_count']}")
            await event.send(event.plain_result(f"✅ 数据库更新成功！\n卡片数量: {result['card_count']}\n\n更新详情:\n{result['output']}"))
        else:
            error_message = result['message']
            logger.error(f"数据库更新失败: {error_message}")
            await event.send(event.plain_result(f"❌ 更新失败: {error_message}\n\n错误信息:\n{result.get('error', '')}"))
