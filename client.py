#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

robot.key = '' or robot.key


# 第01步：导入日志模块 logging
# 定义 logging 的配置
# 日志模块的基本配置
"""参考：
import logging
logging.basicConfig(
    filename="chat.log",  # 日志文件名称
    filemode="a",  # 文件操作方式：追加
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",  # 日志记录的格式
    datefmt="%d-%M-%Y %H:%M:%S",  # 日期格式
    level=logging.DEBUG)  # 日志的级别
"""


def question(prompt='我'):
    """
    接收用户输入的函数
    :param prompt: 默认提示文本
    :return: 提示文本 + 用户从终端输入的内容
    """
    robot.input_text = input(f'{prompt}：')  # 将用户输入赋值给变量

    # 第02步：将 quesiont 写入日志，通过 logging.debug(f'{prompt}：{robot.input_text}')

    return f'{prompt}：{robot.input_text}'  # 必须添加返回值才可以被写入日志


def answer(prompt='机器人'):
    """
    机器人回复的函数
    :param prompt: 默认提示文本
    :return: 提示文本 + 服务器返回的结果
    """
    reply = robot.get_values()

    # 第03步：将 answer 写入日志，通过 logging.debug(f'{prompt}：{reply}')

    return f'{prompt}：{reply}'  # 必须添加返回值才可以被写入日志


# 第01步：
# 定义 chat(master_naem, robot_name, *exit_words) 函数，封装用户姓名，机器人姓名和退出关键字列表
# chat() 函数将之前主函数循环结构的所有代码封装起来
# 主要练习函数参数的使用
def chat(master_name, robot_name, *exit_words):
    pass


if __name__ == '__main__':
    # 第02步：调用定义的 chat() 函数，并给参数赋值
    # 退出关键字元组示例：*('88', '886', 'exit', 'quit')
    pass
