#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 HTTP 服务功能
"""

import asyncio
import json
import sys
import os
import requests

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from mcp.server import FastMCP
from mcp.types import Tool, TextContent
from core import CardQueryCore, config_manager

async def test_http_service():
    """测试 HTTP 服务功能"""
    print("=== 测试 HTTP 服务功能 ===")
    
    # 创建 CardQueryCore 实例
    core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
    
    # 创建 FastMCP 服务器
    server = FastMCP(
        name=config_manager.get('mcp.server_name', 'ygo-card-query-mcp'),
        host='127.0.0.1',
        port=8000
    )
    
    # 注册工具
    @server.tool(
        name="query_card",
        description="查询游戏王卡片信息",
    )
    async def query_card(sql: str = ""):
        """查询游戏王卡片信息"""
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
    
    # 启动服务器
    print("\n1. 启动 HTTP 服务器...")
    import threading
    def run_server():
        server.run(transport='streamable-http')
    
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    # 等待服务器启动
    import time
    time.sleep(2)
    
    # 测试 2: 测试 list_tools 请求
    print("\n2. 测试 list_tools 请求...")
    try:
        response = requests.post(
            'http://localhost:8000/mcp',
            json={
                "jsonrpc": "2.0",
                "method": "list_tools",
                "params": {},
                "id": 1
            }
        )
        result = response.json()
        print(f"   ✅ list_tools 请求成功")
        print(f"   工具数量: {len(result['result'])}")
        for tool in result['result']:
            print(f"   - {tool['name']}: {tool['description'][:50]}...")
    except Exception as e:
        print(f"   ❌ list_tools 请求失败: {e}")
        return False
    
    # 测试 3: 测试 query_card 请求
    print("\n3. 测试 query_card 请求...")
    try:
        response = requests.post(
            'http://localhost:8000/mcp',
            json={
                "jsonrpc": "2.0",
                "method": "call_tool",
                "params": {
                    "name": "query_card",
                    "arguments": {
                        "sql": "SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' LIMIT 3"
                    }
                },
                "id": 2
            }
        )
        result = response.json()
        print(f"   ✅ query_card 请求成功")
        if 'result' in result and 'content' in result['result']:
            content = result['result']['content'][0]['text']
            print(f"   查询结果: {content[:100]}...")
    except Exception as e:
        print(f"   ❌ query_card 请求失败: {e}")
        return False
    
    print("\n=== 所有测试完成 ===")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_http_service())
    if success:
        print("\n🎉 所有测试通过！")
    else:
        print("\n❌ 部分测试失败！")
        sys.exit(1)
