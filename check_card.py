#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查特定卡片的类型
"""

import sqlite3
import os

# 数据库路径
db_path = os.path.join(os.getcwd(), "ygopro-database", "cards.cdb")

if not os.path.exists(db_path):
    print(f"数据库文件不存在: {db_path}")
    exit(1)

# 连接数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查询包含"阿"和"库"的卡片
cursor.execute("SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def FROM datas d JOIN texts t ON d.id = t.id WHERE t.name LIKE '%阿%'")
cards = cursor.fetchall()

print("查询结果:")
for card in cards:
    card_id, name, card_type, attribute, level, race, atk, defense = card
    if "库" in name:
        print(f"ID: {card_id}")
        print(f"名称: {name}")
        print(f"类型: {card_type} (二进制: {card_type:08b})")
        print(f"属性: {attribute}")
        print(f"等级: {level}")
        print(f"种族: {race}")
        print(f"攻击力: {atk}")
        print(f"防御力: {defense}")
        print(f"是否是XYZ怪兽 (type & 64): {bool(card_type & 64)}")
        print(f"是否是连接怪兽 (type & 128): {bool(card_type & 128)}")
        print()

conn.close()
