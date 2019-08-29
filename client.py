#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

robot.key = '' or robot.key


# 第01步：导入日志模块 logging
# 定义 logging 的配置
# 日志模块的基本配置


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
