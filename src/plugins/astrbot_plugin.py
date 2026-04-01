# -*- coding: utf-8 -*-
"""
游戏王查卡插件 - 基于asrtbot
"""

from core import CardQueryCore
from astrbot.api.star import Star, register, StarTools
from astrbot.api.event import filter
from astrbot.core.config.astrbot_config import AstrBotConfig
from astrbot.core.platform.astr_message_event import AstrMessageEvent
import astrbot.api.message_components as Comp
from astrbot.api.all import logger
from typing import Dict, Any, List
import random

@register("astrbot_plugin_ygo_card_query", "Wen", "游戏王查卡插件", "1.0.0")
class CardQueryPlugin(Star):
    def __init__(self, context=None, config: AstrBotConfig = None):
        super().__init__(context, config)
        self.name = "astrbot_plugin_ygo_card_query"
        self.description = "游戏王查卡插件"
        self.version = "1.0.0"
        
        try:
            data_dir = StarTools.get_data_dir()
            logger.info(f"使用数据目录: {data_dir}")
        except Exception as e:
            logger.warning(f"StarTools.get_data_dir() 自动获取失败 ({e})，使用手动路径兜底。")
            data_dir = None
        
        self.core = CardQueryCore(data_dir)
        
        logger.info("CardQuery 插件初始化完成")
    
    async def terminate(self):
        """插件卸载/关闭时的清理工作"""
        logger.info("CardQuery 插件已卸载")
    
    async def _send_text_message(self, event: AstrMessageEvent, message: str):
        """发送文本消息"""
        logger.info("发送查询结果文本")
        await event.send(event.plain_result(message))
    
    def _build_card_info(self, card: Dict, is_ai: bool = False) -> str:
        """构建卡片信息"""
        if is_ai:
            info = f"找到卡片：{card['name']}\n"
            separator = "："
        else:
            info = f"🔍 查询结果: {card['name']}\n"
            separator = ":"
        
        info += f"类型{separator} {card['type']}\n"
        if "ocg_tcg" in card:
            info += f" {card['ocg_tcg']}\n"
        if "tuner" in card:
            info += f"调整{separator} 是\n"
        
        is_monster = "怪兽" in card.get('type', '')
        if is_monster:
            if "attribute" in card:
                info += f"属性{separator} {card['attribute']}\n"
            if "race" in card:
                info += f"种族{separator} {card['race']}\n"
            if "attack" in card:
                info += f"攻击力{separator} {card['attack']}\n"
            if "defense" in card:
                info += f"防御力{separator} {card['defense']}\n"
            if "link" in card:
                info += f"链接{separator} {card['link']}\n"
            elif "rank" in card:
                info += f"阶级{separator} {card['rank']}\n"
            elif "level" in card:
                info += f"等级{separator} {card['level']}\n"
        
        if "description" in card:
            info += f"效果{separator} {card['description']}\n"
        
        if is_ai:
            info += "请根据以上信息回答用户问题，不要添加额外信息。"
        
        return info

    def _get_best_match_card(self, cards: List[Dict], query: str) -> Dict:
        """根据名称匹配度选择最匹配的卡片"""
        if not cards:
            return None
        if len(cards) == 1:
            return cards[0]
        
        query = query.lower().strip()
        
        best_card = cards[0]
        best_score = 0
        
        all_names_same = True
        first_name = cards[0].get('name', '').lower()
        for card in cards:
            if card.get('name', '').lower() != first_name:
                all_names_same = False
                break
        
        for card in cards:
            card_name = card.get('name', '').lower()
            
            score = 0
            
            if query:
                if card_name == query:
                    score = 1000 + random.randint(0, 100)
                elif card_name.startswith(query):
                    score = 900 + len(query) / len(card_name) * 100
                elif query in card_name:
                    score = 800 + len(query) / len(card_name) * 100
                else:
                    matches = sum(1 for c in query if c in card_name)
                    score = matches / len(query) * 500
            else:
                score = random.randint(900, 1100)
            
            if all_names_same:
                score += random.randint(0, 50)
            
            score += max(0, 50 - len(card_name))
            
            if score > best_score:
                best_score = score
                best_card = card
        
        logger.info(f"最佳匹配卡片: {best_card['name']} (匹配分数: {best_score:.2f})")
        return best_card
    
    async def _send_card_info(self, event: AstrMessageEvent, card: Dict, is_random: bool = False):
        """发送卡片信息和图片给用户"""
        response = self._build_card_info(card, is_ai=False)
        card_id = card.get("id")
        
        if card_id:
            image_url = self.core.get_card_image_url(card_id)
            if image_url:
                try:
                    chain = []
                    chain.append(Comp.Image.fromURL(image_url))
                    chain.append(Comp.Plain(response))
                    if is_random:
                        logger.info(f"随机发送卡片图片和文本: {card['name']}")
                    else:
                        logger.info(f"发送卡片图片和文本: {card['name']}")
                    await event.send(event.chain_result(chain))
                    return
                except Exception as e:
                    logger.error(f"发送图片失败: {e}")
        
        await self._send_text_message(event, response)
    
    async def _handle_query_result(self, event: AstrMessageEvent, result: Dict[str, Any], is_tool_call: bool = False, query: str = ""):
        """处理查询结果并发送响应"""
        if result["status"] != "success" or result["count"] == 0:
            logger.info("未找到与查询条件相关的卡片")
            if not is_tool_call:
                await self._send_text_message(event, "⚠️ 未找到与查询条件相关的卡片")
            return "✅ 查询已成功完成，但未找到符合条件的卡片。请直接回复用户，告知未找到相关卡片，并建议检查卡片名称或尝试其他关键词。绝对不要再次调用查询工具。"
        
        if not is_tool_call and not query:
            parts = event.get_message_str().strip().split()
            query = " ".join(parts[1:]) if len(parts) > 1 else ""
        
        cards = result["results"]
        count = result["count"]
        
        card = self._get_best_match_card(cards, query) if count > 1 else cards[0]
        
        await self._send_card_info(event, card, is_random=False)
        
        if not is_tool_call:
            return "查询完成"
        
        card_names = [c["name"] for c in cards[:3]]
        prefix = f"查询成功，找到 {count} 张卡片"
        suffix = "，显示前3张：" if count > 3 else "："
        return prefix + suffix + "、".join(card_names) + "\n\n请根据以上卡片名称回复用户，不要再次调用查询工具。"
    
    @filter.llm_tool(name="query_card")
    async def query_card(self, event: AstrMessageEvent, sql: str = ""):
        """查询游戏王卡片信息。此工具只需调用一次，会返回完整的卡片信息，不需要重复调用。"""

        logger.info(f"开始处理工具调用: query_card, 参数: sql={sql}")
        
        query = ""
        import re
        like_match = re.search(r'LIKE\s+["\']%([^%]+)%["\']', sql, re.IGNORECASE)
        if like_match:
            query = like_match.group(1).strip()
        
        try:
            result = self.core.query_card(sql)
            logger.info(f"查询结果: status={result['status']}, count={result['count']}")
            return await self._handle_query_result(event, result, is_tool_call=True, query=query)
        except Exception as e:
            error_message = str(e)
            logger.error(f"查询出错: {error_message}")
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
