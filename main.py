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
from typing import Dict, Any, List

@register("astrbot_plugin_ygo_card_query", "Wen", "游戏王查卡插件", "1.0.0")
class CardQueryPlugin(Star):
    def __init__(self, context=None, config: AstrBotConfig = None):
        super().__init__(context, config)
        self.name = "astrbot_plugin_ygo_card_query"
        self.description = "游戏王查卡插件"
        self.version = "1.0.0"
        
        # 获取数据目录（使用 plugin_data 目录）
        try:
            data_dir = StarTools.get_data_dir()
            logger.info(f"使用数据目录: {data_dir}")
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
    
    def _get_best_match_card(self, cards: List[Dict], query: str) -> Dict:
        """根据名称匹配度选择最匹配的卡片"""
        if not cards:
            return None
        if len(cards) == 1:
            return cards[0]
        
        # 清理查询字符串
        query = query.lower().strip()
        
        best_card = cards[0]
        best_score = 0
        
        for card in cards:
            card_name = card.get('name', '').lower()
            
            # 计算匹配分数
            score = 0
            
            # 完全匹配得分最高
            if card_name == query:
                score = 1000
            # 以查询字符串开头
            elif card_name.startswith(query):
                score = 900 + len(query) / len(card_name) * 100
            # 包含查询字符串
            elif query in card_name:
                score = 800 + len(query) / len(card_name) * 100
            # 计算相似度（字符匹配数）
            else:
                # 计算有多少个字符匹配
                matches = sum(1 for c in query if c in card_name)
                score = matches / len(query) * 500
            
            # 名称越短，匹配度越高（加分）
            score += max(0, 50 - len(card_name))
            
            if score > best_score:
                best_score = score
                best_card = card
        
        logger.info(f"最佳匹配卡片: {best_card['name']} (匹配分数: {best_score:.2f})")
        return best_card
    
    async def _handle_query_result(self, event: AstrMessageEvent, result: Dict[str, Any], is_tool_call: bool = False, query: str = ""):
        """处理查询结果并发送响应"""
        # 处理查询失败的情况
        if result["status"] != "success":
            error_message = result.get('message', '未知错误')
            logger.error(f"查询出错: {error_message}")
            # 只返回错误信息给工具调用，不向用户发送消息
            return f"查询出错: {error_message}"
        
        # 处理无结果的情况
        if result["count"] == 0:
            logger.info("未找到与查询条件相关的卡片")
            no_result_message = "⚠️ 未找到与查询条件相关的卡片"
            await self._send_text_message(event, no_result_message)
            return no_result_message
        
        # 获取查询字符串（如果不是工具调用）
        if not is_tool_call and not query:
            message_text = event.get_message_str().strip()
            parts = message_text.split() if message_text else []
            if len(parts) > 1:
                query = " ".join(parts[1:])
        
        # 如果有多张卡片，选择匹配度最高的
        if result["count"] > 1 and query:
            logger.info(f"找到 {result['count']} 张卡片，根据名称匹配度选择最佳匹配")
            best_card = self._get_best_match_card(result["results"], query)
            # 替换结果列表为最佳匹配
            result["results"] = [best_card]
            result["count"] = 1
            logger.info(f"选择最佳匹配卡片: {best_card['name']}")
        
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
                # 只返回卡名给 AI，不要返回完整信息
                card_name = result["results"][0]["name"]
                return f"查询成功！找到卡片：{card_name}。请不要再继续调用查询工具。"
            else:
                # 有多张卡片，返回前三张卡片名称
                top_cards = result["results"][:3]
                card_names = [card["name"] for card in top_cards]
                extra_info = f"查询成功！查询到多张卡片，前三张是：{', '.join(card_names)}"
                if result["count"] > 3:
                    extra_info += f" 共找到 {result['count']} 张卡片。请提供更多条件以缩小查询范围。"
                else:
                    extra_info += "。请提供更多条件以缩小查询范围。"
                extra_info += " 请不要再继续调用查询工具。"
                return extra_info
        else:
            return "查询完成"
    
    @filter.llm_tool(name="query_card")
    async def query_card(self, event: AstrMessageEvent, sql: str = ""):
        """查询游戏王卡片信息。当用户询问任何与游戏王卡片相关的问题时，使用此工具查询数据库获取准确的卡片信息。

        Args:
            sql(string): SQL查询语句，必须包含 id, name, type, attribute, level, race, atk, def, desc 字段，必须使用 JOIN 语句连接 datas 和 texts 表，必须使用表别名（如 d.id, t.name）避免列名冲突

        示例：
        - 按名称：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE t.name LIKE '%青眼白龙%'
        - 按属性：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 1 AND d.attribute = 16 （光属性）
        - 按种族：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 1 AND d.race = 8192 （龙族）
        - 按等级：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 1 AND d.level = 8 （8星）
        - 按攻击力：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 1 AND d.atk > 3000
        - 按效果：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE t.desc LIKE '%破坏%'
        - 按卡片类型：SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 2 （魔法卡）
        """
        logger.info(f"开始处理工具调用: query_card, 参数: sql={sql}")
        
        try:
            result = self.core.query_card(sql)
            logger.info(f"查询结果: status={result['status']}, count={result['count']}")
            return await self._handle_query_result(event, result, is_tool_call=True)
        except Exception as e:
            error_message = str(e)
            logger.error(f"查询出错: {error_message}")
            # 只返回错误信息给工具调用，不向用户发送消息
            return f"查询出错: {error_message}"
    
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
            await self._handle_query_result(event, result, query=query)
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
