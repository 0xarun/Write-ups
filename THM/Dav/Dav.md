# Dav Tryhackme Writeup

1. /webdav directory found in gobuster. Webdav is protocol allows users to collaboratively edit and manage files on remote web servers.
2. cadver cmd line to access webdav. login with default creds wampp:xampp
3. Upload reverse shell run it on web
4. www-data shell cat cmd runs as root. sudo /bin/cat /root/root.txt
