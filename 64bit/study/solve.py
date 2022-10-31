from pwn import *
p = remote("remote.goatskin.kr", 31337)
context.log_level = "debug"
p.recvuntil("N =")
N = int(p.recvuntil("\n"))
p.recvuntil("enc(flag) = ")
enc_flag = int(p.recvuntil("\n").strip())
ct = (pow(2,65537,N) * enc_flag) % N
p.sendline(str(ct))
p.recvuntil("decrypted = ")
text = int(p.recvuntil("\n").strip())
text = str(text/2)
print(text)
