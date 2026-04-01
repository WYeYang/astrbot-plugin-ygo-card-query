#!/usr/bin/env python
# -*- coding:#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config =#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name',#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race:#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=6#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=2621#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=10485#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=419#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type:#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=819#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=671088#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=2#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=5#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=10485#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            )
    
    # 如果配置#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            )
    
    # 如果配置文件中没有定义工具，则使用默认工具
    if not tools:
        tools.append(
            Tool(
                name="query_card#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            )
    
    # 如果配置文件中没有定义工具，则使用默认工具
    if not tools:
        tools.append(
            Tool(
                name="query_card",
                description="""查询游戏#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            )
    
    # 如果配置文件中没有定义工具，则使用默认工具
    if not tools:
        tools.append(
            Tool(
                name="query_card",
                description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
游戏王查卡 MCP HTTP 服务器
基于 Model Context Protocol (MCP) 标准
"""

import asyncio
import os
import sys

from mcp.server import Server
from mcp.server.http import http_server
from mcp.types import Tool, TextContent

from core import CardQueryCore, config_manager

# 从配置文件读取MCP服务器配置
mcp_config = config_manager.get_mcp_config()
server_name = mcp_config.get('server_name', 'ygo-card-query-mcp')

app = Server(server_name)

core = CardQueryCore(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


@app.list_tools()
async def list_tools() -> list[Tool]:
    # 从配置文件读取工具列表
    mcp_config = config_manager.get_mcp_config()
    tools_config = mcp_config.get('tools', [])
    
    # 构建工具列表
    tools = []
    for tool_config in tools_config:
        if tool_config.get('name') == 'query_card':
            tools.append(
                Tool(
                    name="query_card",
                    description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: 卡片名称(在texts表)，如 t.name LIKE '%青眼%'
- t.desc: 效果描述(在texts表)，如 t.desc LIKE '%破坏%'
- d.attribute: 属性，地=1,水=2,炎=4,风=8,光=16,暗=32,神=64
- d.race: 种族，战士=1,魔法师=2,天使=4,恶魔=8,不死=16,机械=32,水=64,炎=128,岩石=256,鸟兽=512,植物=1024,昆虫=2048,雷=4096,龙=8192,兽=16384,兽战士=32768,恐龙=65536,鱼=131072,海龙=262144,爬虫=524288,念动力=1048576,幻神兽=2097152,创造神=4194304,幻龙=8388608
- d.type: 类型，怪兽=1,通常=1,效果=33,融合=65,仪式=129,仪式效果=161,同调=8193,同调效果=8225,XYZ=8388609,XYZ效果=8388641,连接=67108865,连接效果=67108897,灵摆=16777233,灵摆效果=16777265,调整=16385,调整效果=16417,魔法=2,通常魔法=2,永续魔法=131074,装备魔法=262146,速攻魔法=65538,场地魔法=524290,仪式魔法=130,陷阱=4,通常陷阱=4,永续陷阱=131076,反击陷阱=1048580
- d.level: 等级/阶级/链接数
- d.atk/d.def: 攻击力/防御力

提示：查单张卡用 ORDER BY RANDOM() LIMIT 1；查多张用 ORDER BY RANDOM() LIMIT 3；搜效果用 t.desc LIKE '%关键词%'；查询时请使用简体中文关键词。

示例：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 3""",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL查询语句"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            )
    
    # 如果配置文件中没有定义工具，则使用默认工具
    if not tools:
        tools.append(
            Tool(
                name="query_card",
                description="""查询游戏王卡片信息。

SQL查询格式：SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE ...

重要字段说明：
- t.name: