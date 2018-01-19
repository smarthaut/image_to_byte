#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 14:23
# @Author  : huanghe
# @Site    : 
# @File    : 2048.py
# @Software: PyCharm
import curses
from random import randrange,choice
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WASDwasdrq']
actions = ['Up','Left','Down','Right','Restart','Exit']
actions_dict = dict(zip(letter_codes,actions * 2))

def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

