# http://blog.csdn.net/u013166622/article/details/51164402
 
import hashlib  
import urllib.request  
import json  

##加密英文  
def md5en(str):  
    m = hashlib.md5()    
    m.update(str.encode(encoding='utf-8'))   
    md5value=m.hexdigest()  
    return md5value  
  
  
##加密中文  
def md5zh(str):  
    m = hashlib.md5()    
    m.update(str.encode(encoding='gb2312'))   
    md5value=m.hexdigest()  
    return md5value  
#翻译成中文  
def autoTozh(q):  
    ##拼接加密字符串  
    str = "2015063000000001" + q + "143566028812345678";  
    sign=md5en(str)  
    ##拼接url  
    url="http://api.fanyi.baidu.com/api/trans/vip/translate?q="+urllib.parse.quote(q)+"&from=auto&to=zh&appid=2015063000000001&salt=1435660288&sign="+sign  
    #print(url)  
    response = urllib.request.urlopen(url).read().decode('utf8')  
    #print(response)  
    getJson = json.loads(response)  
    #print(getJson)  
    getInfo = getJson['trans_result']  
    #print(getInfo)  
    s=getInfo[0]  
    re=s['dst']  
    #print(s)  
    print(re)  
    return re  
  
#翻译成英文  
def autoToen(q):  
    ##拼接加密字符串  
    str = "2015063000000001" + q + "143566028812345678";  
    sign=md5en(str)  
    #print(sign)  
    ##拼接url  
    #URL 只允许一部分 ASCII 字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。 所以 URL 中使用其他字符就需要进行 URL 编码。  
    url="http://api.fanyi.baidu.com/api/trans/vip/translate?q="+urllib.parse.quote(q)+"&from=auto&to=en&appid=2015063000000001&salt=1435660288&sign="+sign  
    #print(url)  
    response = urllib.request.urlopen(url).read()  
    response=response.decode('utf-8')  
    #print(response)  
    getJson = json.loads(response)  
    #print(getJson)  
    getInfo = getJson['trans_result']  
    #print(getInfo)  
    s=getInfo[0]  
    re=s['dst']  
    #print(s)  
    print(re)  
    return re  
  

# b=str(input("输入要翻译词句："))  
# autoToen(b)  
# print('Done') 
