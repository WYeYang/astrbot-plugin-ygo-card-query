#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试游戏王查卡 MCP 服务器
"""

import sys
import json
from io import StringIO

# 保存原始的标准输入和输出
original_stdin = sys.stdin
original_stdout = sys.stdout

# 创建一个字符串缓冲区来模拟标准输入
input_buffer = StringIO()

# 写入初始化请求
input_buffer.write(json.dumps({
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
}) + '\n')

# 写入获取工具列表的请求
input_buffer.write(json.dumps({
    "jsonrpc": "2.0",
    "id": "2",
    "method": "tools/list",
    "params": {}
}) + '\n')

# 写入调用工具的请求
input_buffer.write(json.dumps({
    "jsonrpc": "2.0",
    "id": "3",
    "method": "tools/call",
    "params": {
        "name": "query_card",
        "arguments": {
            "sql": "SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 1"
        }
    }
}) + '\n')

# 将缓冲区指针移到开头
input_buffer.seek(0)

# 重定向标准输入到我们的缓冲区
sys.stdin = input_buffer

# 创建一个字符串缓冲区来捕获标准输出
output_buffer = StringIO()
sys.stdout = output_buffer

# 导入并运行服务器
import ygo_mcp.server

try:
    # 运行服务器
    ygo_mcp.server.main()
except Exception as e:
    print(f"错误: {e}")
finally:
    # 恢复原始的标准输入和输出
    sys.stdin = original_stdin
    sys.stdout = original_stdout

# 打印捕获的输出
print("服务器输出:")
print(output_buffer.getvalue())
