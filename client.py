#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""
import logging

import tuling_robot as robot

robot.key = '' or robot.key

logging.basicConfig(
    filename="chat.log",  # 日志文件名称
    filemode="a",  # 文件操作方式：追加
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",  # 日志记录的格式
    datefmt="%d-%M-%Y %H:%M:%S",  # 日期格式
    level=logging.DEBUG)  # 日志的级别


# 第01步（困难）：定义装饰器函数 log()，装饰目标函数，将目标函数的返回值写入日志


# 第02步：装饰 question() 函数，将用户输入的问题写入日志
def question(prompt='我'):
    """
    接收用户输入的函数
    :param prompt: 默认提示文本
    :return: 提示文本 + 用户从终端输入的内容
    """
    robot.input_text = input(f'{prompt}：')  # 将用户输入赋值给变量
    return f'{prompt}：{robot.input_text}'  # 必须添加返回值才可以被写入日志


# 第03步：装饰 answer() 函数，将机器人的回答写入日志
def answer(prompt='机器人'):
    """
    机器人回复的函数
    :param prompt: 默认提示文本
    :return: 提示文本 + 服务器返回的结果
    """
    reply = robot.get_values()
    return f'{prompt}：{reply}'  # 必须添加返回值才可以被写入日志


def chat(master_name, robot_name, *exit_words):
    while True:
        question(master_name)

        if robot.input_text in exit_words:
            print(robot_name, '：拜拜~~')
            break
        elif not robot.input_text:
            continue
        else:
            print(answer(robot_name))


if __name__ == '__main__':
    chat('我', '阿拉蕾', *('88', '886', 'exit', 'quit'))
