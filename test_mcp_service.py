#!/usr/bin/env python
# -*- coding#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP 服务功能 ===")
    
    # 测试 1: 测试#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP 服务功能 ===")
    
    # 测试 1: 测试配置文件加载
    print("\n#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP 服务功能 ===")
    
    # 测试 1: 测试配置文件加载
    print("\n1. 测试配置文件加载...")
    try:
        database_config =#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ygo_mcp.server import main as mcp_main
from core import CardQueryCore, config_manager

async def test_mcp_service():
    """测试 MCP 服务功能"""
    print("=== 测试 MCP 服务功能 ===")
    
    # 测试 1: 测试配置文件加载
    print("\n1. 测试配置文件加载...")
    try:
        database_config = config_manager.get_database_config()
        card_query_config = config_manager.get_card_query_config#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

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
        print(f#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

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
        print(f"   ✅ 配置文件加载成功")#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 MCP 服务功能
"""

import asyncio
import json
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

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
        print