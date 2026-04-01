#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from ..core import CardQueryCore

app = Server("ygo-card-query-mcp")

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
core.db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ygopro_database")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="query_card",
            description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "SQL查询语句"
                    }
                },
                "required": ["sql"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    try:
        if name == "query_card":
            sql = arguments.get("sql", "")
            result = core.query_card(sql)
            
            if result["status"] != "success" or result["count"] == 0:
                return [TextContent(
                    type="text",
                    text="未找到符合条件的卡片。请检查查询条件或尝试其他关键词。"
                )]
            
            cards = result["results"]
            count = result["count"]
            
            output_lines = [f"查询成功，找到 {count} 张卡片：\n"]
            
            for i, card in enumerate(cards[:10], 1):
                output_lines.append(f"\n{i}. {card['name']}")
                output_lines.append(f"   类型: {card['type']}")
                if 'attribute' in card and card['attribute'] != '无':
                    output_lines.append(f"   属性: {card['attribute']}")
                if 'race' in card and card['race'] != '无':
                    output_lines.append(f"   种族: {card['race']}")
                if 'attack' in card:
                    output_lines.append(f"   攻击力: {card['attack']}")
                if 'defense' in card:
                    output_lines.append(f"   防御力: {card['defense']}")
                if 'level' in card:
                    output_lines.append(f"   等级: {card['level']}")
                elif 'rank' in card:
                    output_lines.append(f"   阶级: {card['rank']}")
                elif 'link' in card:
                    output_lines.append(f"   链接: {card['link']}")
                if 'description' in card:
                    desc = card['description'][:200] + "..." if len(card['description']) > 200 else card['description']
                    output_lines.append(f"   效果: {desc}")
            
            if count > 10:
                output_lines.append(f"\n... 还有 {count - 10} 张卡片未显示")
            
            return [TextContent(type="text", text="\n".join(output_lines))]
        
        else:
            return [TextContent(type="text", text=f"未知工具: {name}")]
    
    except Exception as e:
        return [TextContent(type="text", text=f"执行出错: {str(e)}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
