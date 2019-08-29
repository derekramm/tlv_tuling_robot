#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""client.py"""

import tuling_robot as robot

robot.key = '' or robot.key

if __name__ == '__main__':

    # 第01步：使用 死循环（无限循环）实现重复聊天的效果
    robot.input_text = input('我：')
    if robot.input_text in ['88', '886', 'exit', 'quit']:
        print('机器人：', '拜拜~~')
        # 第02步：使用循环控制语句 break 终端循环
    elif not robot.input_text:
        # 第03步：使用循环控制语句 continue 跳出本次循环继续下次循环
        pass
    else:
        print('机器人：', robot.get_values())
