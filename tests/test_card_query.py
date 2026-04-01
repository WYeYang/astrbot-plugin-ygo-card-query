# -*- coding: utf-8 -*-
"""
测试游戏王查卡核心功能
"""

import unittest
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ygo_card_query.core import CardQueryCore

class TestCardQueryCore(unittest.TestCase):
    """测试 CardQueryCore 类的核心功能"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.test_dir = os.getcwd()
        print(f"\n测试数据目录: {self.test_dir}")
        
        self.core = CardQueryCore()
    
    def test_update_database(self):
        """测试更新数据库方法（数据库已存在时执行 git pull）"""
        print("\n=== 测试更新数据库（git pull） ===")
        
        db_dir = os.path.join(self.test_dir, "ygopro-database")
        print(f"数据库目录: {db_dir}")
        print(f"数据库目录是否存在: {os.path.exists(db_dir)}")
        
        result = self.core.update_database()
        print(f"更新结果: {result}")
        
        self.assertEqual(result["status"], "success")
        self.assertIn("数据库更新成功", result["message"])
        
        self.assertTrue(os.path.exists(db_dir), f"数据库目录不存在: {db_dir}")
        
        cdb_path = os.path.join(db_dir, "locales", "zh-CN", "cards.cdb")
        print(f"数据库文件路径: {cdb_path}")
        print(f"数据库文件是否存在: {os.path.exists(cdb_path)}")
        self.assertTrue(os.path.exists(cdb_path), f"数据库文件不存在: {cdb_path}")
        
        print("数据库更新测试通过（git pull）")
    
    def test_update_database_clone(self):
        """测试更新数据库方法（无数据库时执行 git clone）"""
        print("\n=== 测试更新数据库（git clone） ===")
        
        test_clone_dir = os.path.join(self.test_dir, "test_clone_data")
        if os.path.exists(test_clone_dir):
            shutil.rmtree(test_clone_dir)
        os.makedirs(test_clone_dir, exist_ok=True)
        
        core = CardQueryCore(test_clone_dir)
        
        print(f"测试克隆目录: {test_clone_dir}")
        print(f"数据库目录: {core.db_dir}")
        
        result = core.update_database()
        print(f"更新结果: {result}")
        
        self.assertEqual(result["status"], "success")
        self.assertIn("数据库更新成功", result["message"])
        
        self.assertTrue(os.path.exists(core.db_dir), f"数据库目录不存在: {core.db_dir}")
        
        cdb_path = os.path.join(core.db_dir, "locales", "zh-CN", "cards.cdb")
        print(f"数据库文件路径: {cdb_path}")
        print(f"数据库文件是否存在: {os.path.exists(cdb_path)}")
        self.assertTrue(os.path.exists(cdb_path), f"数据库文件不存在: {cdb_path}")
        
        if os.path.exists(test_clone_dir):
            shutil.rmtree(test_clone_dir)
            print(f"清理测试目录: {test_clone_dir}")
        
        print("数据库更新测试通过（git clone）")
    
    def test_query_card(self):
        """测试查询卡片方法"""
        print("\n=== 测试查询卡片 ===")
        
        cdb_path = os.path.join(self.test_dir, "ygopro-database", "locales", "zh-CN", "cards.cdb")
        if not os.path.exists(cdb_path):
            print("数据库不存在，跳过测试（需要手动调用 update_database 更新）")
            self.skipTest("数据库不存在")
        
        print("测试默认查询...")
        result = self.core.query_card()
        print(f"默认查询结果: 找到 {result['count']} 张卡片")
        self.assertEqual(result["status"], "success")
        self.assertGreater(result["count"], 0)
        
        print("测试 SQL 查询...")
        sql = """
            SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
            FROM datas d 
            JOIN texts t ON d.id = t.id
            WHERE t.name LIKE '%青眼白龙%'
        """
        result = self.core.query_card(sql)
        print(f"SQL查询结果: 找到 {result['count']} 张卡片")
        self.assertEqual(result["status"], "success")
        self.assertGreaterEqual(result["count"], 0)
        
        print("卡片查询测试通过")
    
    def test_get_card_image_url(self):
        """测试获取卡片图片 URL 方法"""
        print("\n=== 测试获取卡片图片 URL ===")
        card_id = 46986414
        print(f"测试卡片ID: {card_id}")
        
        image_url = self.core.get_card_image_url(card_id)
        expected_url = f"https://cdn.233.momobako.com/ygopro/pics/{card_id}.jpg"
        
        print(f"生成的URL: {image_url}")
        print(f"期望的URL: {expected_url}")
        
        self.assertEqual(image_url, expected_url)
        print("卡片图片 URL 测试通过")

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    
    unittest.main(verbosity=2)
