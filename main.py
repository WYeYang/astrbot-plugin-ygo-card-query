# -*- coding: utf-8 -*-
"""
游戏王自然语言查卡插件 - 基于asrtbot
"""

from .card_query import CardQueryPlugin


def get_plugin():
    return CardQueryPlugin()