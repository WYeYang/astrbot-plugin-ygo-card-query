#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查连接怪兽的类型标识
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

# 查询所有攻击力为0或者防御力为0的怪兽，可能是连接怪兽
cursor.execute("""
    SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def 
    FROM datas d 
    JOIN texts t ON d.id = t.id 
    WHERE d.type & 1 
    AND (d.def = 0 OR d.def IS NULL)
    AND d.atk > 0
    LIMIT 20
""")
cards = cursor.fetchall()

print("可能是连接怪兽的卡片:")
for card in cards:
    card_id, name, card_type, attribute, level, race, atk, defense = card
    print(f"ID: {card_id}, 名称: {name}")
    print(f"  类型: {card_type} (二进制: {card_type:032b})")
    print(f"  等级: {level}, 攻击力: {atk}, 防御力: {defense}")
    print()

# 也查询一些已知的连接怪兽名称
cursor.execute("""
    SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def 
    FROM datas d 
    JOIN texts t ON d.id = t.id 
    WHERE t.name LIKE '%解码%' OR t.name LIKE '%编码%' OR t.name LIKE '%防火%'
    LIMIT 10
""")
cards = cursor.fetchall()

print("\n已知可能是连接怪兽的卡片:")
for card in cards:
    card_id, name, card_type, attribute, level, race, atk, defense = card
    print(f"ID: {card_id}, 名称: {name}")
    print(f"  类型: {card_type} (二进制: {card_type:032b})")
    print(f"  等级: {level}, 攻击力: {atk}, 防御力: {defense}")
    print()

conn.close()
