# 游戏王查卡插件

## 功能介绍

这是一个为 AstrBot 设计的游戏王查卡插件，允许用户通过命令或 SQL 查询来获取游戏王卡片信息。

## 项目结构

```
astrbot-plugin-ygo-card-query/
├── src/                   # 源代码目录
│   ├── config/            # 配置文件目录
│   │   ├── config.yaml                  # 插件配置文件
│   │   └── mcp_config_example.json      # MCP配置示例文件
│   ├── core/              # 核心功能模块
│   │   ├── __init__.py                  # 包初始化文件
│   │   ├── card_query.py                # 卡片查询核心实现
│   │   └── config.py                    # 配置管理
│   ├── plugins/           # 插件实现
│   │   ├── __init__.py                  # 包初始化文件
│   │   ├── astrbot_plugin.py            # AstrBot插件实现
│   │   ├── main.py                      # 插件入口
│   │   └── metadata.yaml                # 插件元数据
│   └── ygo_mcp/           # MCP服务实现
│       ├── __init__.py                  # 包初始化文件
│       ├── deploy.bat                   # Windows部署脚本
│       ├── deploy.sh                    # Linux/macOS部署脚本
│       ├── mcp_server.py                # MCP服务器实现
│       └── server.py                    # MCP服务入口
├── test/                  # 测试目录
├── README.md              # 插件说明文档
├── requirements.txt       # 依赖项
├── pyproject.toml         # 项目配置文件
└── merge_summary.md       # 合并摘要
```

## 功能特性

- 支持通过自然语言查询卡片（例如：`/查卡 青眼白龙`）
- 提供 `query_card` LLM 工具函数，支持 SQL 查询
- 自动克隆和更新游戏王卡片数据库（从 GitHub 仓库）
- 支持查询卡片图片
- 支持按卡片名称、类型、属性、攻击力等进行查询

## 安装方法

### 方法一：作为 AstrBot 插件安装
1. 将 `src/plugins` 目录复制到 AstrBot 的插件目录中
2. 重启 AstrBot 即可使用
3. 首次使用时会自动克隆 ygopro-database 数据库（可能需要一些时间）

### 方法二：使用 MCP 服务
1. 安装依赖：`pip install uv`
2. 运行 MCP 服务：`uvx git+https://github.com/WYeYang/astrbot-plugin-ygo-card-query.git@feat/mcp-config-update -- python -m ygo_mcp.server`
3. 或者使用部署脚本：
   - Linux/macOS: `src/ygo_mcp/deploy.sh`
   - Windows: `src/ygo_mcp/deploy.bat`

## 使用示例

### 示例1：通过命令查询卡片

```
用户：/查卡 青眼白龙
Bot：返回青眼白龙的卡片信息和图片
```

### 示例2：通过 LLM 工具查询

```python
# 在 LLM 中调用 query_card 工具
sql = """
SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
FROM datas d 
JOIN texts t ON d.id = t.id
WHERE t.name LIKE '%青眼白龙%'
"""
result = await tool.query_card(sql=sql)
```

### 示例3：更新卡片数据库

```
用户：/更新卡片数据库
Bot：开始更新数据库，并返回更新结果
```

## 数据库说明

- 插件使用 [ygopro-database](https://github.com/moecube/ygopro-database) 作为数据源
- 首次初始化时会自动从 GitHub 克隆数据库
- 支持手动更新数据库（使用 `/更新卡片数据库` 命令）
- 数据库包含卡片基本信息和文本描述

## 技术实现

- 使用 SQLite 直接查询卡片数据库
- 支持实时输出克隆和更新过程
- 错误处理机制确保稳定运行
- 不依赖任何外部 Python 包

## 注意事项

- 首次克隆数据库可能需要一些时间，请耐心等待
- 更新数据库需要网络连接
- 数据库文件较大，确保有足够的存储空间

## MCP 配置

### 什么是 MCP
MCP (Model Context Protocol) 是一种用于与模型上下文交互的协议，本插件提供了 MCP 服务支持，可以通过 MCP 协议与插件进行交互。

### 配置文件
MCP 配置文件位于 `src/config/mcp_config_example.json`，您可以根据需要修改配置：

```json
{
  "mcpServers": {
    "ygo-card-query": {
      "command": "uvx",
      "args": [
        "git+https://github.com/WYeYang/astrbot-plugin-ygo-card-query.git@feat/mcp-config-update",
        "--",
        "python",
        "-m",
        "ygo_mcp.server"
      ],
      "cwd": "/tmp"
    }
  }
}
```

### 部署 MCP 服务

#### 方法一：使用部署脚本
- Linux/macOS: 运行 `src/ygo_mcp/deploy.sh`
- Windows: 运行 `src/ygo_mcp/deploy.bat`

#### 方法二：手动部署
1. 安装依赖：`pip install uv`
2. 运行 MCP 服务：`uvx git+https://github.com/WYeYang/astrbot-plugin-ygo-card-query.git@feat/mcp-config-update -- python -m ygo_mcp.server`

### MCP 服务功能
- 提供卡片查询接口
- 支持通过 MCP 协议与插件进行交互
- 可集成到其他支持 MCP 的系统中
- 支持 Streamable HTTP 传输方式

### Streamable HTTP 配置

Streamable HTTP 配置文件位于 `src/config/streamable_http_config.json`，您可以根据需要修改配置：

```json
{
  "mcpServers": {
    "ygo-card-query-http": {
      "type": "streamableHttp",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

### 启动 Streamable HTTP 服务

```bash
# 使用配置文件启动
uvx git+https://github.com/WYeYang/astrbot-plugin-ygo-card-query.git@feat/mcp-config-update -- python -m ygo_mcp.server --transport streamable-http

# 或者使用环境变量
MCP_HOST=127.0.0.1 MCP_PORT=8000 python -m ygo_mcp.server --transport streamable-http
```

## 免责声明

### 数据来源
- **卡片数据**：使用 [ygopro-database](https://github.com/moecube/ygopro-database) 作为数据源
- **卡片图片**：通过 [https://cdn.233.momobako.com/ygopro/pics/](https://cdn.233.momobako.com/ygopro/pics/) 获取卡片图片

### 免责声明
1. 本插件仅用于学习和娱乐目的，不用于商业用途
2. 所有卡片数据和图片的版权归其各自的所有者所有
3. 本插件不保证数据的准确性和完整性，如有错误请以官方资料为准
4. 如因使用本插件产生任何问题，本插件作者不承担任何责任
5. 如您是相关内容的版权所有者，且认为本插件侵犯了您的权益，请联系我们，我们将立即处理

### 版权信息
- 游戏王（Yu-Gi-Oh!）及其相关内容为 KONAMI 公司的注册商标
- 本插件为非官方工具，与 KONAMI 公司无任何关联