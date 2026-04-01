# -*- coding: utf-8 -*-
"""
配置管理模块
负责读取和解析配置文件
"""

import os
import platform
import yaml
from typing import Dict, Any


class ConfigManager:
    """配置管理类"""
    
    def __init__(self, config_path: str = None):
        """
        初始化配置管理器
        
        Args:
            config_path: 配置文件路径，如果为None则使用默认路径
        """
        if config_path is None:
            # 获取平台信息
            current_platform = platform.system().lower()
            
            # 构建平台特定的配置文件路径
            config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "config")
            platform_config_path = os.path.join(config_dir, f"config_{current_platform}.yaml")
            default_config_path = os.path.join(config_dir, "config.yaml")
            
            # 优先使用平台特定的配置文件，如果不存在则使用默认配置文件
            if os.path.exists(platform_config_path):
                config_path = platform_config_path
                print(f"使用平台特定配置文件: {config_path}")
            else:
                config_path = default_config_path
                print(f"使用默认配置文件: {config_path}")
        
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """
        加载配置文件
        
        Returns:
            配置字典
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config or {}
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值
        
        Args:
            key: 配置键，支持点号分隔的嵌套键
            default: 默认值
            
        Returns:
            配置值或默认值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_database_config(self) -> Dict[str, Any]:
        """
        获取数据库配置
        
        Returns:
            数据库配置字典
        """
        return self.get('database', {})
    
    def get_card_query_config(self) -> Dict[str, Any]:
        """
        获取卡片查询配置
        
        Returns:
            卡片查询配置字典
        """
        return self.get('card_query', {})
    
    def get_mcp_config(self) -> Dict[str, Any]:
        """
        获取MCP服务器配置
        
        Returns:
            MCP服务器配置字典
        """
        return self.get('mcp', {})
    
    def get_logging_config(self) -> Dict[str, Any]:
        """
        获取日志配置
        
        Returns:
            日志配置字典
        """
        return self.get('logging', {})


# 创建全局配置实例
config_manager = ConfigManager()
