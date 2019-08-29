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


def log(func):
    def wrapper(*args):  # 练习不定长参数
        result = func(*args)
        logging.debug(result)
        return result  # 这里不要忘记 return

    return wrapper  # 注意不要加括号


@log
def question(prompt='我'):
    """
    接收用户输入的函数
    :param prompt: 默认提示文本
    :return: 提示文本 + 用户从终端输入的内容
    """
    robot.input_text = input(f'{prompt}：')  # 将用户输入赋值给变量
    return f'{prompt}：{robot.input_text}'  # 必须添加返回值才可以被写入日志


@log
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
