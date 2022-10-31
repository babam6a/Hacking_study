import hashlib

target = '2016a'

candidate = 0

while True:

    plaintext = str(candidate)

    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()

    if hash[:5] == target:

        print('plaintext:"' + plaintext + '", md5:' + hash)

        break

    candidate = candidate + 1

