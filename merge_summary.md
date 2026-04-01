此次合并主要实现了从传统插件架构向MCP服务架构的转变，添加了配置管理系统，并重构了卡片查询核心功能。变更包括新增配置文件、MCP服务器实现、项目结构优化，以及完善的文档和测试覆盖。
| 文件 | 变更 |
|------|---------|
| README.md | - 添加了详细的免责声明部分，包括数据来源、版权信息和使用条款 |
| pyproject.toml | - 新增项目配置文件，定义了项目依赖和构建系统 |
| requirements.txt | - 新增依赖文件，指定了MCP和PyYAML的版本要求 |
| src/config/config.yaml | - 新增配置文件，包含数据库、卡片查询、MCP服务器和日志配置 |
| src/config/mcp_config_example.json | - 新增MCP配置示例文件 |
| src/core/__init__.py | - 新增核心模块初始化文件 |
| src/core/card_query.py | - 重构卡片查询核心功能，支持从配置文件读取设置，改进数据库更新和查询逻辑 |
| src/core/config.py | - 新增配置管理模块，提供统一的配置读取和管理功能 |
| src/plugins/__init__.py | - 新增插件模块初始化文件 |
| src/plugins/astrbot_plugin.py | - 简化插件实现，移除冗余代码 |
| src/plugins/main.py | - 新增插件主文件 |
| src/plugins/metadata.yaml | - 新增插件元数据文件 |
| src/ygo_mcp/__init__.py | - 新增MCP模块初始化文件 |
| src/ygo_mcp/deploy.bat | - 新增Windows部署脚本 |
| src/ygo_mcp/deploy.sh | - 新增Linux部署脚本 |
| src/ygo_mcp/mcp_server.py | - 新增MCP服务器入口文件 |
| src/ygo_mcp/server.py | - 新增MCP服务器实现，提供卡片查询工具 |
| test/test_http_service.py | - 新增HTTP服务测试文件 |
| test/test_mcp_service.py | - 新增MCP服务测试文件 |
| test/test_uvx_deployment.py | - 新增UVX部署测试文件 |
| .gitignore | - 更新git忽略文件配置 |
| __init__.py | - 删除根目录初始化文件 |
| test_card_query.py | - 删除旧的测试文件 |