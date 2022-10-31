#! /usr/bin/env sagemath
# load values

import ast
with open('pubkey.txt') as fh:
    b = ast.literal_eval(fh.read())
with open('ciphertext.txt') as fh:
    c = int(fh.read())
n = len(b)
print '[*] pubkey: b =', b
print '[*] ciphertext: c =', c

# check the density
d = float(n / log(max(b), 2))
print '[*] density: d =', d


# low-density attack, CLOS method
# prepare a basis
MULTIPLIER = 100
B = matrix(ZZ, n + 1, n + 1)
B.set_block(0, 0, MULTIPLIER * matrix(n, 1, b))
B.set_block(n, 0, MULTIPLIER * matrix([ - c ]))
B.set_block(0, 1, 2 * identity_matrix(n))
B.set_block(n, 1, matrix([ -1 ] * n))
print '[*] basis: B =', B

# LLL algorithm
for x in B.LLL():
    if x[0] == 0 and all(x_i in [-1, +1] for x_i in x[1 :]):
        print '[*] found: x =', x

        # decode x
        m = 0
        for x_i in reversed(x[1 :]):
            m *= 2
            m += int(x_i == +1)
        print '[*] plaintext: m =', m
        print '[*]', repr(hex(m).decode('hex'))
