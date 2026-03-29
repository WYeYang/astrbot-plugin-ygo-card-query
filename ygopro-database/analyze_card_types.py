#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析游戏王卡片类型标识脚本
"""

import sqlite3
import os

# 数据库路径
db_path = os.path.join(os.getcwd(), "ygopro-database", "cards.cdb")

if not os.path.exists(db_path):
    print(f"数据库文件不存在: {db_path}")
    exit(1)

print(f"分析数据库: {db_path}")
print("=" * 60)

# 连接数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查询不同类型的卡片
print("分析卡片类型标识...")
print("=" * 60)

# 查询怪兽卡片的类型标识
cursor.execute("SELECT DISTINCT type FROM datas WHERE type & 1")
monster_types = cursor.fetchall()

print("怪兽卡片类型标识:")
for (type_id,) in monster_types:
    print(f"类型标识: {type_id:08b} (十进制: {type_id})")

print("\n" + "=" * 60)

# 查询一些具体的卡片示例
print("查询不同类型的怪兽卡片示例:")
print("=" * 60)

# 普通怪兽
cursor.execute("SELECT d.id, t.name, d.type FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 1 AND NOT d.type & 64 AND NOT d.type & 128 AND NOT d.type & 256 LIMIT 3")
normal_monsters = cursor.fetchall()
print("普通怪兽:")
for card_id, name, card_type in normal_monsters:
    print(f"ID: {card_id}, 名称: {name}, 类型标识: {card_type:08b}")

print()

# XYZ怪兽（超量）
cursor.execute("SELECT d.id, t.name, d.type FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 64 LIMIT 3")
xyz_monsters = cursor.fetchall()
print("XYZ怪兽（超量）:")
for card_id, name, card_type in xyz_monsters:
    print(f"ID: {card_id}, 名称: {name}, 类型标识: {card_type:08b}")

print()

# 连接怪兽
try:
    cursor.execute("SELECT d.id, t.name, d.type FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 128 LIMIT 3")
    link_monsters = cursor.fetchall()
    print("连接怪兽:")
    for card_id, name, card_type in link_monsters:
        print(f"ID: {card_id}, 名称: {name}, 类型标识: {card_type:08b}")
except Exception as e:
    print(f"查询连接怪兽失败: {e}")

print()

# 同调怪兽
try:
    cursor.execute("SELECT d.id, t.name, d.type FROM datas d JOIN texts t ON d.id = t.id WHERE d.type & 256 LIMIT 3")
    synchro_monsters = cursor.fetchall()
    print("同调怪兽:")
    for card_id, name, card_type in synchro_monsters:
        print(f"ID: {card_id}, 名称: {name}, 类型标识: {card_type:08b}")
except Exception as e:
    print(f"查询同调怪兽失败: {e}")

print("\n" + "=" * 60)
print("分析完成！")

# 关闭数据库连接
conn.close()
