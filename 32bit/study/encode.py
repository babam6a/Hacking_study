from pwn import *
from hashlib import *


def salt() : 
    for k in range(256):
        salt1 = chr(k)
        for j in range(256) :
            salt2 = chr(j)
            str1 = str(salt1) + str(salt2) + '0|||guest'
            print(str1)
            if hashlib.md5(str1).hexdigest() == 'e54dde85e3a343f897eeb008588aad4e' :
                print(str1)
                print('done!')
                break
    print('done!')

salt()
