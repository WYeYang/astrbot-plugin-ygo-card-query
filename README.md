# 游戏王查卡插件

## 功能介绍

这是一个为 AstrBot 设计的游戏王查卡插件，允许用户通过命令或 SQL 查询来获取游戏王卡片信息。

## 项目结构

```
astrbot-plugin-ygo-card-query/
├── card_query.py          # 插件核心实现
├── card_query_core.py     # 查卡核心功能模块
├── main.py                # 插件入口
├── metadata.yaml          # 插件配置文件
├── requirements.txt       # 依赖项（当前为空）
├── test_card_query.py     # 测试文件
└── README.md              # 插件说明文档
```

## 功能特性

- 支持通过自然语言查询卡片（例如：`/查卡 青眼白龙`）
- 提供 `query_card` LLM 工具函数，支持 SQL 查询
- 自动克隆和更新游戏王卡片数据库（从 GitHub 仓库）
- 支持查询卡片图片
- 支持按卡片名称、类型、属性、攻击力等进行查询

## 安装方法

1. 将插件目录复制到 AstrBot 的插件目录中
2. 重启 AstrBot 即可使用
3. 首次使用时会自动克隆 ygopro-database 数据库（可能需要一些时间）

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