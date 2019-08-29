#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

robot.key = '' or robot.key


# 第01步：
# 定义 quesiont() 函数，通过 input(prompt='我')函数接收输入，并赋值给 robot.input_text 变量
# question() 函数中需要返回用户的输入
def question(prompt='我'):  # 练习默认值参数
    pass


# 第02步：
# 定义 answer() 函数，通过 get_values() 函数接收服务器端返回的结果
# answer() 函数中需要返回机器人回复的结果
def answer(prompt='机器人'):  # 练习默认值参数
    pass


if __name__ == '__main__':

    while True:
        # 第03步：此处调用 quesiont() 函数

        if robot.input_text in ['88', '886', 'exit', 'quit']:
            print('机器人：', '拜拜~~')
            break
        elif not robot.input_text:
            continue
        else:
            # 第04步：此处调用 answer() 函数

            pass
