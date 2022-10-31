from pwn import *


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def mulinv(a, b):
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

p = remote("remote.goatskin.kr", 10474)
context.log_level = "debug"

p.recvuntil("flag!\n")

for i in range(21) :
    a = p.recvuntil(" ").strip()
    op = p.recvuntil("x = ")
    b = p.recvuntil(" ").strip()
    p.recvuntil("(mod ")
    N = p.recvuntil(")").strip(b")")

    if "+" in op : 
        answer = int(b)-int(a)
        if answer<0 : 
            answer = answer + int(N)
    elif "-" in op :
        answer =int(a)-int(b)
        if answer<=0 : 
            answer = answer + int(N)
    elif "*" in op : 
        answer = int(b)* mulinv(int(a),int(N))
    print(answer)
    p.sendline(str(answer))
    p.recvuntil("Correct!\n")
