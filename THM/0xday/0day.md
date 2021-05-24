# 0day
https://tryhackme.com/room/0day

#### Nmap

	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)
	|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
	|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
	|_  256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
	80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
	| http-methods: 
	|_  Supported Methods: GET HEAD POST OPTIONS
	|_http-server-header: Apache/2.4.7 (Ubuntu)
	|_http-title: 0day
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


## User Exploit:

1. Use Msfmoudle *exploit/multi/http/apache_mod_cgi_bash_env_exec*
2. set options and run after we got meterpreter then open shell

User Shell!

## Root Exploit

1. Kernel Exploit *Kernel version: 3.13.0*
2. search ExploitDB https://www.exploit-db.com/exploits/37292
3. Run the exploit

Root Shell!
