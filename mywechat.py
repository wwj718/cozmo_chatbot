import itchat
from IPython import embed
from pinyin_tool import zh_to_pinyin
from baidu_translate import autoToen
from http_tool import post_content_to_cozmo

@itchat.msg_register(itchat.content.TEXT,isFriendChat=True, isGroupChat=False, isMpChat=False)
def text_reply(msg):
    # print(msg.actualNickName)
    content = msg.text
    # print(content)
    nickname = msg.User.NickName
    # content = "{}说{}".format(nickname,content)
    content = "{}".format(content)
    tr_content  = zh_to_pinyin(content)
    # tr_content = autoToen(content) # export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
    print(tr_content)
    post_content_to_cozmo(tr_content)
    # return msg.text
    # make request to cozmo server

itchat.auto_login(hotReload=True)
itchat.run()
