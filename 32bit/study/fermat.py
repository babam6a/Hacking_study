#!/usr/bin/python
# coding: utf-8

from gmpy2 import *

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n


def fermat_factor(n):
    assert n % 2 != 0
    a = isqrt(n)
    b2 = square(a) - n
    while not is_square(b2):
        a += 1
        b2 = square(a) - n
    p = a + isqrt(b2)
    q = a - isqrt(b2)
    return int(p), int(q)

def main():
    n = int("d0e2a38e5094e98cf80d7b298bb15d1f48ca6b12910cd599b246fe30dc81e966072d526bd0fc92243119564ad7cbe7b4990c51eff617ca75bf02834b09631b72d23a84e3ff6c8f82c65f8cc53a3f58135e56c1330b3084533c660c9b40fc22c31da64dc98bf00a8c4726dcc5a8e2f7c9535c939b64857529dadf66f0778a420d",16)
    """e = int("10001",16)
    #c = int("334d41a2fb325d0e7586e026bb50c9dd3bc97c50d492bb1456274b2579777898336e16526944d72ac5315a8ba4e696e9b7824fad7decd21f3bdcd76f32639430220c2b79ed889209384732fdfb570ee5d8d77e524b35983a23a22524d6421fa1e9fea01e8098a9e8a47e14137354a406c25c8cc1e0887a0c81d727dd01d313a83",16)
"""
    
    p, q = fermat_factor(n)
    phi_n = (p - 1) * (q - 1)
    print phi_n

"""
    d = mulinv(e, phi_n)
    decrypted_msg = powmod(c, d, n)

    print "[*] p / q :", float(p) / float(q)
    print hex(decrypted_msg).replace('0x', '').decode('hex')
"""

if __name__ == '__main__':
    main() 
