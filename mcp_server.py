#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP 服务器 - 入口文件
基于 Model Context Protocol (MCP) 标准
"""

from ygo_card_query.mcp import main

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
