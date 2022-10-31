from pwn import *
import base64

context.log_level="debug"

p = remote("ubuntu32.goatskin.kr",7531);

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
changed_string = ""
p.recvuntil('String for encryption\n')
p.sendline("RmFrZUZsYWcgOkQgSEFIQSBJIHdpbGwgdXNlIGFub3RoZXIgb25l")
p.recvuntil('String for encryption\n')
code = "Vd40Sn/jsfVP80JZbfoTyhirNIrEK5mp2zo/9C26Ibr8Vuaku9"
decrypted_code = ""

for i in range(len(code)) :
    for j in range(len(string)) :
        p.sendline(string[j]*(i+1))
        p.recvuntil(" : ")
        n = p.recvuntil("\n").strip()[-1]
        if n == code[i] :
            decrypted_code += string[j]
            break;
print(decrypted_code)
