#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys
import argparse
from typing import Any

from mcp.server import FastMCP
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 解析命令行参数
parser = argparse.ArgumentParser(description='游戏王查卡 MCP 服务器')
parser.add_argument('--transport', type=str, default='stdio', choices=['stdio', 'streamable-http'],
                    help='传输方式 (默认: stdio)')
parser.add_argument('--host', type=str, default='127.0.0.1',
                    help='服务器主机 (默认: 127.0.0.1)')
parser.add_argument('--port', type=int, default=8000,
                    help='服务器端口 (默认: 8000)')
args = parser.parse_args()

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

# 创建FastMCP服务器
app = FastMCP(
    name=server_name,
    host=args.host,
    port=args.port
)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.add_tool
async def query_card(sql: str) -> list[TextContent]:
    try:
        result = core.query_card(sql)
        
        if result["status"] != "success" or result["count"] == 0:
            return [TextContent(
                type="text",
                text="未找到符合条件的卡片。请检查查询条件或尝试其他关键词。"
            )]
        
        cards = result["results"]
        count = result["count"]
        
        # 从配置文件读取最大返回结果数
        card_query_config = config_manager.get_card_query_config()
        max_results = card_query_config.get('max_results', 10)
        
        output_lines = [f"查询成功，找到 {count} 张卡片：\n"]
        
        for i, card in enumerate(cards[:max_results], 1):
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
        
        if count > max_results:
            output_lines.append(f"\n... 还有 {count - max_results} 张卡片未显示")
        
        return [TextContent(type="text", text="\n".join(output_lines))]
    
    except Exception as e:
        return [TextContent(type="text", text=f"执行出错: {str(e)}")]


def main():
    # 运行 Streamable HTTP 服务器
    app.run(transport='streamable-http')


if __name__ == "__main__":
    main()
