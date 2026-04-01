#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP 服务功能 ===")
    
    # 测试 1: 测试配置文件加载
    print("\n1. 测试配置文件加载...")
    try:
        database_config = config_manager.get_database_config()
        card_query_config = config_manager.get_card_query_config()
        mcp_config = config_manager.get_mcp_config()
        print(f"   ✅ 配置文件加载成功")
        print(f"   数据库配置: {database_config}")
        print(f"   卡片查询配置: {card_query_config}")
        print(f"   MCP 配置: {mcp_config}")
    except Exception as e:
        print(f"   ❌ 配置文件加载失败: {e}")
        return False
    
    # 测试 2: 测试 CardQueryCore 初始化
    print("\n2. 测试 CardQueryCore 初始化...")
    try:
        core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
        print(f"   ✅ CardQueryCore 初始化成功")
        print(f"   数据目录: {core.data_dir}")
        print(f"   数据库目录: {core.db_dir}")
    except Exception as e:
        print(f"   ❌ CardQueryCore 初始化失败: {e}")
        return False
    
    # 测试 3: 测试卡片查询功能
    print("\n3. 测试卡片查询功能...")
    try:
        # 测试默认查询
        default_result = core.query_card()
        print(f"   ✅ 默认查询成功，找到 {default_result['count']} 张卡片")
        
        # 测试特定卡片查询
        sql = "SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' LIMIT 3"
        specific_result = core.query_card(sql)
        print(f"   ✅ 特定查询成功，找到 {specific_result['count']} 张卡片")
        if specific_result['count'] > 0:
            print(f"   示例卡片: {[card['name'] for card in specific_result['results'][:3]]}")
    except Exception as e:
        print(f"   ❌ 卡片查询失败: {e}")
        return False
    
    # 测试 4: 测试卡片图片 URL 生成
    print("\n4. 测试卡片图片 URL 生成...")
    try:
        card_id = 46986414  # 青眼白龙的卡片 ID
        image_url = core.get_card_image_url(card_id)
        print(f"   ✅ 图片 URL 生成成功: {image_url}")
    except Exception as e:
        print(f"   ❌ 图片 URL 生成失败: {e}")
        return False
    
    # 测试 5: 测试 MCP 服务启动
    print("\n5. 测试 MCP 服务启动...")
    try:
        # 这里我们不实际启动服务，只是检查导入是否成功
        print(f"   ✅ MCP 服务模块导入成功")
        print(f"   服务名称: {config_manager.get('mcp.server_name', 'ygo-card-query-mcp')}")
    except Exception as e:
        print(f"   ❌ MCP 服务导入失败: {e}")
        return False
    
    print("\n=== 所有测试完成 ===")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_mcp_service())
    if success:
        print("\n🎉 所有测试通过！")
    else:
        print("\n❌ 部分测试失败！")
        sys.exit(1)
