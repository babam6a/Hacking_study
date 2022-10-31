from pwn import *

def start() :
    p = remote("remote.goatskin.kr", 52150)
    context.log_level = "debug"
    p.recvuntil("Flag : ")
    temp = p.recvuntil("\n")
    flag = int(temp, 16)
    p.recvuntil("(4) Exit")
    p.sendline("1")
    p.recvuntil("n : ")
    temp = p.recvuntil("\n")
    n = int(temp, 16)
    p.recvuntil("g : ")
    temp = p.recvuntil("\n")
    g = int(temp,16)
    p.recvuntil("(4) Exit")
    p.sendline("2")
    p.recvuntil("format :")
    p.sendline("1\n")
    p.recvuntil("Encrypted : ")
    temp = p.recvuntil("\n")
    enc = int(temp, 16)
    p.recvuntil("(4) Exit")

    return flag,n,g,enc,p

def cal(flag,n,g,enc,p) :
    new = flag * enc
    send = new % (n**2)
    send_hex = hex(send).lstrip("0x") + "\n"
    p.sendline("3")
    p.recvuntil("format :")
    p.sendline(send_hex)
    p.recvuntil("Decrypted : ")
    result = p.recvuntil("\n")
    return result

def main() : 
    flag,n,g,enc,p = start()
    temp = cal(flag,n,g,enc,p)
    ans = hex(int(temp, 16) - 1).lstrip("0x").decode("hex")
    print(ans)
    
main()
