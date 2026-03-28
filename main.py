# -*- coding: utf-8 -*-
"""
游戏王查卡插件 - 基于asrtbot
"""

from .card_query import CardQueryPlugin


def get_plugin():
    return CardQueryPlugin
