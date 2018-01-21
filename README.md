# cozmo_chatbot

说明: cozmo目前只能say_text("英文")

遇到中文问题，可以先把中文转化为拼音

# 通用工具
*  cozmo作为一个web server，等待请求，可以来自ifttt，也可以来自其他进程(itchat)

# 项目
*  让cozmo读出微信消息
*  ifttt控制播报新闻

# test

`http http://127.0.0.1:5001/cozmo_say content="zao shang hao ， ha ha"`

# 微信机器人使用说明
先启动微信进程

然后启动cozmo web server进程