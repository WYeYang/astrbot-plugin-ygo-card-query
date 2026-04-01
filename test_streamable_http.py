#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试游戏王查卡 MCP 服务器 (Streamable HTTP 模式)
"""

import httpx
import json
import time

async def test_mcp_server():
    # 服务器URL
    server_url = "http://localhost:8000/mcp"
    
    print("测试游戏王查卡 MCP 服务器 (Streamable HTTP 模式)")
    print(f"服务器地址: {server_url}")
    print("=" * 50)
    
    # 创建一个HTTP客户端
    async with httpx.AsyncClient() as client:
        # 1. 建立SSE连接
        print("1. 建立SSE连接...")
        response = await client.get(
            server_url,
            headers={
                "Accept": "text/event-stream",
                "Cache-Control": "no-cache"
            },
            timeout=None
        )
        
        # 检查连接是否成功
        if response.status_code != 200:
            print(f"连接失败: {response.status_code}")
            return
        
        # 提取会话ID
        session_id = response.headers.get("X-Session-ID")
        if not session_id:
            print("无法获取会话ID")
            return
        
        print(f"会话ID: {session_id}")
        print("连接成功!")
        print("=" * 50)
        
        # 2. 发送初始化请求
        print("2. 发送初始化请求...")
        init_request = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": "initialize",
            "params": {
                "protocolVersion": "2.0",
                "capabilities": {},
                "clientInfo": {
                    "name": "test",
                    "version": "1.0"
                }
            }
        }
        
        init_response = await client.post(
            server_url,
            headers={
                "Content-Type": "application/json",
                "X-Session-ID": session_id
            },
            json=init_request
        )
        
        print(f"初始化响应: {init_response.json()}")
        print("=" * 50)
        
        # 3. 获取工具列表
        print("3. 获取工具列表...")
        list_tools_request = {
            "jsonrpc": "2.0",
            "id": "2",
            "method": "tools/list",
            "params": {}
        }
        
        list_tools_response = await client.post(
            server_url,
            headers={
                "Content-Type": "application/json",
                "X-Session-ID": session_id
            },
            json=list_tools_request
        )
        
        print(f"工具列表响应: {list_tools_response.json()}")
        print("=" * 50)
        
        # 4. 测试查询卡片功能
        print("4. 测试查询卡片功能...")
        query_card_request = {
            "jsonrpc": "2.0",
            "id": "3",
            "method": "tools/call",
            "params": {
                "name": "query_card",
                "arguments": {
                    "sql": "SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 1"
                }
            }
        }
        
        query_card_response = await client.post(
            server_url,
            headers={
                "Content-Type": "application/json",
                "X-Session-ID": session_id
            },
            json=query_card_request
        )
        
        print(f"查询卡片响应: {query_card_response.json()}")
        print("=" * 50)
        
        print("测试完成!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_mcp_server())
