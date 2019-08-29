#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

robot.key = '' or robot.key

if __name__ == '__main__':
    # 通过用户输入赋值 robot.input_text 属性
    robot.input_text = input('我：')

    # 第01步：通过 if 语句检查输入的合法性和有效性
    # 如果输入的文本是：['88','886','exit','quit'] 其中的一个，输出信息：'拜拜~~'
    # 如果输入的文本为空（直接回车），则直接使用 pass 忽略
    # 如果输入其它文本，则调用机器人接口函数 get_values() 并打印
    robot.get_values()
