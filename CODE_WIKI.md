# 游戏王查卡插件 - Code Wiki

## 目录
1. [项目概述](#1-项目概述)
2. [项目架构](#2-项目架构)
3. [主要模块说明](#3-主要模块说明)
4. [核心类与函数](#4-核心类与函数)
5. [数据库结构](#5-数据库结构)
6. [依赖关系](#6-依赖关系)
7. [项目运行方式](#7-项目运行方式)

---

## 1. 项目概述

### 1.1 项目简介
游戏王查卡插件是一个为 AstrBot 设计的游戏王卡片查询插件，允许用户通过命令或 SQL 查询来获取游戏王卡片信息。该插件集成了自动数据库更新、卡片图片展示和智能匹配等功能。

### 1.2 主要特性
- 通过自然语言命令查询卡片（如 `/查卡 青眼白龙`）
- 提供 `query_card` LLM 工具函数，支持灵活的 SQL 查询
- 自动克隆和更新游戏王卡片数据库（从 GitHub 仓库）
- 支持查询并展示卡片图片
- 按卡片名称、类型、属性、攻击力等多种条件查询
- 智能匹配功能，从多个结果中选择最匹配的卡片

### 1.3 项目信息
- **名称**: astrbot_plugin_ygo_card_query
- **显示名称**: 游戏王查卡
- **版本**: 1.0.0
- **作者**: Wen
- **仓库**: https://github.com/WYeYang/astrbot-plugin-ygo-card-query

---

## 2. 项目架构

### 2.1 目录结构
```
astrbot-plugin-ygo-card-query/
├── __init__.py              # 包初始化文件
├── main.py                  # 插件入口和主要业务逻辑
├── card_query_core.py       # 查卡核心功能模块
├── test_card_query.py       # 单元测试文件
├── metadata.yaml            # 插件配置元数据
├── requirements.txt         # Python依赖项（当前为空）
├── README.md                # 项目说明文档
├── .gitignore               # Git忽略文件
├── .gitmodules              # Git子模块配置
└── ygopro_database/         # 数据库目录
    ├── cards.cdb            # 卡片数据库（SQLite）
    └── card_extra.db        # 额外卡片数据库
```

### 2.2 架构设计
项目采用分层架构设计，主要分为三层：

1. **插件层** ([main.py](file:///workspace/main.py))
   - 负责 AstrBot 插件的注册和事件处理
   - 处理用户命令和 LLM 工具调用
   - 构建卡片信息展示格式
   - 管理卡片图片的发送

2. **核心功能层** ([card_query_core.py](file:///workspace/card_query_core.py))
   - 提供独立的数据库查询和管理功能
   - 不依赖 AstrBot，可单独使用
   - 处理 Git 克隆和更新操作
   - 封装 SQLite 数据库访问

3. **数据层**
   - 从 [ygopro-database](https://github.com/moecube/ygopro-database) 获取数据
   - 使用 SQLite 存储卡片信息
   - 支持多语言（主要使用 zh-CN）

### 2.3 数据流
```
用户命令/LLM工具调用
    ↓
插件层 (main.py) - 处理事件、构建查询
    ↓
核心功能层 (card_query_core.py) - 执行SQL查询、数据转换
    ↓
数据层 - SQLite数据库访问
    ↓
返回处理结果
    ↓
插件层 - 构建响应信息、发送卡片和图片
```

---

## 3. 主要模块说明

### 3.1 main.py - 插件主模块
**职责**:
- 注册 AstrBot 插件
- 处理用户命令（`/查卡`、`/更新卡片数据库`）
- 注册 LLM 工具函数 `query_card`
- 构建卡片信息展示
- 发送文本和图片消息

**关键功能**:
- 命令过滤器处理
- 智能卡片匹配
- 卡片信息格式化
- 图片URL生成和发送

### 3.2 card_query_core.py - 核心功能模块
**职责**:
- 管理游戏王数据库的克隆和更新
- 提供卡片查询接口
- 数据格式转换（数字编码→可读文本）
- 卡片图片URL生成
- 独立于 AstrBot，可作为通用模块使用

**关键功能**:
- Git 命令执行（克隆/拉取）
- SQLite 数据库查询
- 卡片类型、属性、种族的解码
- 卡片图片CDN链接生成

### 3.3 test_card_query.py - 测试模块
**职责**:
- 单元测试核心功能
- 验证数据库更新功能
- 测试卡片查询逻辑
- 验证图片URL生成

---

## 4. 核心类与函数

### 4.1 CardQueryPlugin 类 (main.py)
**类说明**: 游戏王查卡插件主类，继承自 AstrBot 的 Star 类。

**主要方法**:

#### `__init__(self, context=None, config: AstrBotConfig = None)`
- **功能**: 初始化插件，设置数据目录，初始化核心功能模块
- **参数**:
  - `context`: AstrBot 上下文
  - `config`: AstrBot 配置对象
- **关键逻辑**:
  - 尝试通过 `StarTools.get_data_dir()` 获取数据目录
  - 初始化 `CardQueryCore` 实例

#### `handle_cha_ka(self, event: AstrMessageEvent)`
- **装饰器**: `@filter.command("查卡", alias={"/查卡"})`
- **功能**: 处理 `/查卡` 命令，按卡片名称查询
- **参数**: `event` - AstrBot 消息事件对象
- **SQL示例**:
  ```sql
  SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
  FROM datas d 
  JOIN texts t ON d.id = t.id
  WHERE t.name LIKE '%查询关键词%'
  ```

#### `handle_update_database(self, event: AstrMessageEvent)`
- **装饰器**: `@filter.command("更新卡片数据库", alias={"/更新卡片数据库"})`
- **功能**: 处理数据库更新命令
- **参数**: `event` - AstrBot 消息事件对象
- **流程**: 发送开始更新消息 → 调用 `core.update_database()` → 返回更新结果

#### `query_card(self, event: AstrMessageEvent, sql: str = "")`
- **装饰器**: `@filter.llm_tool(name="query_card")`
- **功能**: LLM 工具函数，支持灵活的 SQL 查询
- **参数**:
  - `event`: AstrBot 消息事件对象
  - `sql`: SQL 查询语句
- **返回值**: 查询结果的文本描述，用于 LLM 回复

#### `_get_best_match_card(self, cards: List[Dict], query: str) -> Dict`
- **功能**: 根据卡片名称匹配度选择最匹配的卡片
- **参数**:
  - `cards`: 卡片列表
  - `query`: 查询字符串
- **评分规则**:
  - 完全匹配: 1000 + 随机值
  - 以查询开头: 900 + 长度比例分
  - 包含查询: 800 + 长度比例分
  - 其他: 字符匹配度分
- **加分项**: 名称越短得分越高

#### `_build_card_info(self, card: Dict, is_ai: bool = False) -> str`
- **功能**: 构建卡片信息字符串
- **参数**:
  - `card`: 卡片信息字典
  - `is_ai`: 是否为 AI 调用模式
- **返回值**: 格式化的卡片信息文本

### 4.2 CardQueryCore 类 (card_query_core.py)
**类说明**: 游戏王查卡核心功能类，不依赖 AstrBot，可独立使用。

**主要方法**:

#### `__init__(self, data_dir=None)`
- **功能**: 初始化核心功能，设置数据目录
- **参数**: `data_dir` - 数据存储目录，默认使用当前工作目录
- **数据库路径**: `{data_dir}/ygopro-database`

#### `update_database(self) -> Dict[str, Any]`
- **功能**: 更新游戏王数据库
- **返回值**: 包含状态、消息、输出的字典
- **流程**:
  1. 检查数据库目录是否存在
  2. 存在则执行 `git pull` 更新
  3. 不存在则执行 `git clone` 克隆
  4. 返回操作结果

#### `_execute_git_command(self, cmd, cwd, description)`
- **功能**: 异步执行 Git 命令并实时输出日志
- **参数**:
  - `cmd`: Git 命令列表
  - `cwd`: 工作目录
  - `description`: 命令描述（用于日志）
- **特点**: 逐字符读取输出，处理回车符更新进度

#### `query_card(self, sql: str = "") -> Dict[str, Any]`
- **功能**: 执行卡片查询
- **参数**: `sql` - SQL 查询语句
- **返回值**:
  ```python
  {
      "status": "success",
      "query": sql,
      "results": [卡片信息列表],
      "count": 卡片数量,
      "note": "备注信息"
  }
  ```
- **关键转换**:
  - 卡片类型位掩码解析
  - 属性数字→中文映射
  - 种族数字→中文映射
  - OCG/TCG 标识解析

#### `get_card_image_url(self, card_id: int) -> str`
- **功能**: 获取卡片图片 URL
- **参数**: `card_id` - 卡片 ID
- **返回值**: CDN 图片链接
- **格式**: `https://cdn.233.momobako.com/ygopro/pics/{card_id}.jpg`

### 4.3 辅助函数和内部类

#### Logger 类 (card_query_core.py)
- **功能**: 模拟日志接口，用于独立使用时的日志输出
- **方法**: `info()`, `error()`, `warning()`

---

## 5. 数据库结构

### 5.1 数据源
- **仓库**: https://github.com/moecube/ygopro-database
- **语言**: zh-CN（简体中文）
- **格式**: SQLite

### 5.2 数据表结构

#### datas 表 - 卡片基本信息
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 卡片ID（主键） |
| type | INTEGER | 卡片类型（位掩码） |
| attribute | INTEGER | 属性（位掩码） |
| level | INTEGER | 等级/阶级/链接数 |
| race | INTEGER | 种族（位掩码） |
| atk | INTEGER | 攻击力 |
| def | INTEGER | 防御力 |
| ot | INTEGER | OCG/TCG 标识 |

#### texts 表 - 卡片文本信息
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 卡片ID（外键，关联 datas.id） |
| name | TEXT | 卡片名称 |
| desc | TEXT | 卡片效果描述 |

### 5.3 编码映射表

#### 属性映射 (attribute)
| 值 | 属性 |
|----|------|
| 0 | 无 |
| 1 | 地 |
| 2 | 水 |
| 4 | 炎 |
| 8 | 风 |
| 16 | 光 |
| 32 | 暗 |

#### 种族映射 (race)
| 值 | 种族 |
|----|------|
| 1 | 战士 |
| 2 | 魔法师 |
| 4 | 天使 |
| 8 | 恶魔 |
| 16 | 不死 |
| 32 | 机械 |
| 64 | 水 |
| 128 | 炎 |
| 256 | 岩石 |
| 512 | 鸟兽 |
| 1024 | 植物 |
| 2048 | 昆虫 |
| 4096 | 雷 |
| 8192 | 龙 |
| 16384 | 兽 |
| 32768 | 兽战士 |
| 65536 | 恐龙 |
| 131072 | 鱼 |
| 262144 | 海龙 |
| 524288 | 爬虫 |
| 1048576 | 念动力 |
| 2097152 | 幻神兽 |
| 4194304 | 创造神 |
| 8388608 | 幻龙 |

#### 卡片类型位掩码 (type)
| 位 | 值 | 说明 |
|----|-----|------|
| 0 | 1 | 怪兽 |
| 1 | 2 | 魔法 |
| 2 | 4 | 陷阱 |
| 6 | 64 | 融合 |
| 7 | 128 | 仪式 |
| 13 | 8192 | 同调 |
| 14 | 16384 | 调整 |
| 19 | 524288 | 场地 |
| 20 | 1048576 | 速攻/反击 |
| 21 | 2097152 | 永续 |
| 22 | 4194304 | 装备 |
| 23 | 8388608 | XYZ |
| 24 | 16777216 | 灵摆 |
| 26 | 67108864 | 连接 |

---

## 6. 依赖关系

### 6.1 Python 依赖
项目无外部 Python 依赖，使用 Python 标准库：
- `os` - 文件系统操作
- `sqlite3` - SQLite 数据库访问
- `subprocess` / `asyncio.subprocess` - 子进程执行
- `threading` - 线程支持
- `time` - 时间操作
- `random` - 随机数生成
- `re` - 正则表达式
- `typing` - 类型提示

### 6.2 系统依赖
- **Git**: 用于克隆和更新数据库
- **AstrBot**: 运行插件的宿主平台（核心模块可独立使用）

### 6.3 AstrBot API 依赖
- `astrb.api.star.Star` - 插件基类
- `astrb.api.star.register` - 插件注册装饰器
- `astrb.api.star.StarTools` - 插件工具类
- `astrb.api.event.filter` - 事件过滤器
- `astrb.core.config.astrbot_config.AstrBotConfig` - 配置类
- `astrb.core.platform.astr_message_event.AstrMessageEvent` - 消息事件
- `astrb.api.message_components` - 消息组件
- `astrb.api.all.logger` - 日志记录器

### 6.4 外部服务
- **GitHub**: 数据库源码仓库
- **CDN**: 卡片图片服务 (cdn.233.momobako.com)

---

## 7. 项目运行方式

### 7.1 安装与部署

#### 作为 AstrBot 插件安装
1. 将插件目录复制到 AstrBot 的插件目录
2. 重启 AstrBot
3. 首次使用会自动克隆数据库（需要网络连接）

#### 核心模块独立使用
```python
from card_query_core import CardQueryCore

# 初始化核心模块
core = CardQueryCore(data_dir="/path/to/data")

# 更新数据库
import asyncio
result = asyncio.run(core.update_database())

# 查询卡片
sql = "SELECT * FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%青眼%'"
result = core.query_card(sql)

# 获取卡片图片
image_url = core.get_card_image_url(46986414)
```

### 7.2 使用方式

#### 命令查询
```
用户: /查卡 青眼白龙
Bot: 返回卡片信息和图片
```

#### 数据库更新
```
用户: /更新卡片数据库
Bot: 开始更新，并返回更新结果
```

#### LLM 工具调用
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

### 7.3 运行测试
```bash
python test_card_query.py
```

### 7.4 注意事项
1. 首次克隆数据库可能需要较长时间
2. 更新数据库需要网络连接
3. 数据库文件较大，确保有足够存储空间
4. 插件不依赖外部 Python 包，使用标准库即可运行

---

## 附录

### A. SQL 查询示例

#### 按名称查询
```sql
SELECT d.id, t.name, d.type, d.attribute, d.level, d.race, d.atk, d.def, t.desc 
FROM datas d 
JOIN texts t ON d.id = t.id
WHERE t.name LIKE '%青眼%'
```

#### 查询特定属性的怪兽
```sql
SELECT * FROM datas d JOIN texts t ON d.id = t.id 
WHERE d.attribute = 16  -- 光属性
AND d.type & 1 = 1      -- 怪兽卡
ORDER BY RANDOM() LIMIT 5
```

#### 查询效果包含关键词的卡片
```sql
SELECT * FROM datas d JOIN texts t ON d.id = t.id 
WHERE t.desc LIKE '%破坏%'
ORDER BY RANDOM() LIMIT 3
```

### B. 常用卡片 ID
- 青眼白龙: 46986414
- 黑魔术师: 46986415
- 死者苏生: 83764718

---

*文档版本: 1.0.0*  
*最后更新: 2026-04-01*
