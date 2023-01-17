# Simple Touhou Project Controller - 东方 Project 简易外设

## 1. 介绍
Simple Touhou Project Controller 是一个可以将手机作为外设，游玩 **东方 Project** 的程序。
此项目目前处于屎山状态，之后可能会找时间重新写。

## 2. 使用
要求 `flask` `pywinio` 模块，`pywinio` 必须正确配置。
以管理员模式 Python 运行 `keyboard_service.py` ，然后再运行 `app.py`。
flask 控制台此时会输出一个位于局域网的IP。访问 `IP:host\ui` 即可。
键位配置在 `config.ini`。

## 3. 其他
按键模拟直接使用了示例代码。