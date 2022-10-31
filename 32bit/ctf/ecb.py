from pwn import *
import base64

p = remote("tasks.aeroctf.com",44323)
#context.log_level = "debug"

p.recvuntil("Exit\n")
def three(salt) :
    p.sendline("3")
    p.recvuntil("salt: ")
    p.sendline(salt)
    p.recvuntil("secret: b")
    return p.recvuntil("\n").rstrip()
origin = base64.b64decode(three("").encode())
for i in range(8) :
    msg = "a"*i
    new = base64.b64decode(three(msg).encode())
    print("[+]" + new)


p.interactive()
