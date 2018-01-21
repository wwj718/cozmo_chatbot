from pypinyin import lazy_pinyin
'''
from googletrans import Translator # 需要翻墙换了吧
translator = Translator()
translator.translate('早上好', src='zh-cn')
'''

def zh_to_pinyin(content):
    # zh_string = "早上好"
    pinyin_string = ' '.join(lazy_pinyin(content))
    return pinyin_string

# 使用百度吧
'''
def zh_to_english(content):
    # export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
    en = translator.translate(content, src='zh-cn').text
    return en    
'''
# print(zh_to_pinyin("早上好，哈哈"))

# robot.say_text(pinyin_string).wait_for_completed()
