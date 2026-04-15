# 游戏王查卡 MCP 服务器 - ModelScope部署指南

## 部署配置

以下是ModelScope平台的部署配置：

```json
{
  "name": "游戏王AI查卡",
  "description": "AI 智能查询游戏王卡牌信息，支持卡名、效果、类型检索",
  "icon": "https://cdn-1309233702.cos.ap-guangzhou.myqcloud.com/game/icon/game-yugioh.png",
  "runtime": "python3",
  "deployType": "streamableHttp",
  "host": "0.0.0.0",
  "port": 8000,
  "path": "/mcp",
  "command": "cd src/ygo_mcp && python -m ygo_mcp.server --transport streamable-http --host 0.0.0.0 --port 8000",
  "resources": {
    "cpu": 1,
    "memory": 1024
  },
  "autoStart": true,
  "protocol": "http"
}
```

## 配置文件说明

### 1. MCP服务器配置文件
位置：`src/config/config.yaml`

这个文件包含：
- 数据库配置：游戏王卡片数据库的位置和更新源
- 卡片查询配置：SQL查询语句和返回结果限制
- MCP服务器配置：服务器名称和工具定义

### 2. MCP客户端配置文件
位置：`src/config/streamable_http_config.json`

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

## 部署前准备

1. **数据库初始化**：
   运行 `deploy.sh install` 来安装依赖和初始化数据库
   ```bash
   cd src/ygo_mcp
   ./deploy.sh install
   ```

2. **测试服务器**：
   在本地测试服务器是否正常运行
   ```bash
   ./deploy.sh run
   ```

## 部署步骤

1. 将整个项目上传到ModelScope平台
2. 使用上述配置文件创建MCP服务器
3. 等待部署完成
4. 测试MCP服务器的功能

## 功能说明

### 可用工具

1. **query_card**：查询游戏王卡片信息
   - 参数：`sql` - SQL查询语句
   - 示例：
     ```sql
     SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%' ORDER BY RANDOM() LIMIT 1
     ```

### 数据库字段说明

- `t.name`：卡片名称
- `t.desc`：卡片效果描述
- `d.attribute`：属性（地=1,水=2,炎=4,风=8,光=16,暗=32,神=64）
- `d.race`：种族
- `d.type`：卡片类型
- `d.level`：等级/阶级/链接数
- `d.atk`：攻击力
- `d.def`：防御力

## 常见问题

1. **数据库下载失败**：
   - 检查网络连接
   - 确保有足够的磁盘空间

2. **服务器启动失败**：
   - 检查端口8000是否被占用
   - 查看日志文件获取详细错误信息

3. **查询返回空结果**：
   - 检查SQL查询语句是否正确
   - 确保数据库已正确初始化
