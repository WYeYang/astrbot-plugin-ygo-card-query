#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单的测试脚本，使用项目中的现有数据库
"""

import os
import sys

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from card_query_core import CardQueryCore

def test_existing_database():
    """测试使用项目中已有的数据库"""
    print("=" * 60)
    print("测试使用项目中已有的数据库")
    print("=" * 60)
    
    # 使用当前目录，数据库在 ygopro_database 文件夹
    core = CardQueryCore()
    
    # 修改数据库路径以匹配实际位置
    core.db_dir = os.path.join(os.getcwd(), "ygopro_database")
    print(f"使用数据库目录: {core.db_dir}")
    
    # 检查数据库文件
    cdb_path = os.path.join(core.db_dir, "cards.cdb")
    print(f"数据库文件路径: {cdb_path}")
    
    if not os.path.exists(cdb_path):
        print(f"❌ 数据库文件不存在: {cdb_path}")
        return False
    
    print(f"✅ 数据库文件存在")
    
    # 测试查询功能
    try:
        print("\n--- 测试默认查询 ---")
        result = core.query_card()
        print(f"状态: {result['status']}")
        print(f"找到卡片数: {result['count']}")
        
        if result['count'] > 0:
            print(f"\n第一张卡片: {result['results'][0]['name']}")
        
        print("\n✅ 默认查询测试通过")
        
        # 测试按名称查询
        print("\n--- 测试按名称查询 (青眼) ---")
        sql = """
            SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
            FROM datas d 
            JOIN texts t ON d.id = t.id
            WHERE t.name LIKE '%青眼%'
        """
        result = core.query_card(sql)
        print(f"状态: {result['status']}")
        print(f"找到卡片数: {result['count']}")
        
        if result['count'] > 0:
            print(f"\n找到的卡片:")
            for card in result['results']:
                print(f"  - {card['name']}")
        
        print("\n✅ 按名称查询测试通过")
        
        # 测试图片URL生成
        print("\n--- 测试图片URL生成 ---")
        if result['count'] > 0:
            card_id = result['results'][0]['id']
            image_url = core.get_card_image_url(card_id)
            print(f"卡片ID: {card_id}")
            print(f"图片URL: {image_url}")
            print("✅ 图片URL生成测试通过")
        
        print("\n" + "=" * 60)
        print("所有测试通过！")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_existing_database()
    sys.exit(0 if success else 1)
