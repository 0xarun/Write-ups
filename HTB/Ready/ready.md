# Ready Writeup (notes)

https://app.hackthebox.eu/machines/Ready

#### Nmap

    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)  
    |   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
    |_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
    5080/tcp open  http    nginx
    | http-robots.txt: 53 disallowed entries (15 shown)
    | / /autocomplete/users /search /api /admin /profile 
    | /dashboard /projects/new /groups/new /groups/*/edit /users /help 
    |_/s/ /snippets/new /snippets/*/edit
    | http-title: Sign in \xC2\xB7 GitLab
    |_Requested resource was http://10.10.10.220:5080/users/sign_in
    |_http-trane-info: Problem with XML parsing of /evox/about
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

open port http 5080 its GitLab....

lets google find any some exploit for gitlab got one exploit in exploitdb

    GitLab 11.4.7 - RCE (Authenticated) (2) 
   https://www.exploit-db.com/exploits/49334


its was perfectly working and got shell and too user.txt

lets go for privsec

/opt/backups heres some files gitlab.rb in this file i got smtp_password using this password login with root yeah root password as well...


tbh i dont know what to do next cause after root there was a dark no files. dont hesitate to see writeup and I done this box using this writeup and take notes what you learn.. 

### ready writeup

https://hackingwebservice.wordpress.com/2021/01/03/htb-ready-hackthebox-writeup/

So we will create a test folder inside /tmp directory and will mount the /dev/sda2 in it and we can simply cat out the root.txt file

    $ mkdir /tmp/test
    $ mount /dev/sda2
    $ cat /tmp/test/root/root.txt

