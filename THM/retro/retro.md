# Retro 

https://tryhackme.com/room/retro

#### Nmap

	PORT     STATE SERVICE       REASON  VERSION
	80/tcp   open  http          syn-ack Microsoft IIS httpd 10.0
	| http-methods: 
	|   Supported Methods: OPTIONS TRACE GET HEAD POST
	|_  Potentially risky methods: TRACE
	|_http-title: IIS Windows Server
	3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
	| rdp-ntlm-info: 
	|   Target_Name: RETROWEB
	|   NetBIOS_Domain_Name: RETROWEB
	|   NetBIOS_Computer_Name: RETROWEB
	|   DNS_Domain_Name: RetroWeb
	|   DNS_Computer_Name: RetroWeb
	|   Product_Version: 10.0.14393
	|_  System_Time: 2021-05-13T12:43:26+00:00
	| ssl-cert: Subject: commonName=RetroWeb
	| Issuer: commonName=RetroWeb
	| Public Key type: rsa
	| Public Key bits: 2048
	| Signature Algorithm: sha256WithRSAEncryption
	| Not valid before: 2021-05-12T12:39:35
	| Not valid after:  2021-11-11T12:39:35
	| MD5:   81b9 28ab acf5 2a44 f35a dc83 dc9d d6ea
	| SHA-1: e9e6 8d10 7084 54da 91ac a8ca 6b48 a47b cb86 df6f
	| -----BEGIN CERTIFICATE-----
	| MIIC1DCCAbygAwIBAgIQOTRb4vfIcotLcB3AcNO+NjANBgkqhkiG9w0BAQsFADAT
	| MREwDwYDVQQDEwhSZXRyb1dlYjAeFw0yMTA1MTIxMjM5MzVaFw0yMTExMTExMjM5
	| MzVaMBMxETAPBgNVBAMTCFJldHJvV2ViMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
	| MIIBCgKCAQEAmxkSGWh8sAzkyHXzVkgdwh6MrFxIIbFBYwX0NavkoixlPTWPZRVh
	| y+eXHcq4cTOtq6GGlLzqqqhAMCxTzj0pZCM3xlYfkkQBR2ToXex1HXsTUxCLYaV/
	| d7j01KA1xLvcla5ckfzgrdc8Hi01+QmSWvJ0qD2fOJpWboTjax4LwWFA7sGDxCby
	| WeMzininshjAUwLjEr+TtCs+pM8G24VnDRyZ+UXZwfmaotkKvVTkRyGprzDYwKdm
	| ScQ5JUMkZivZAdQXKI93lwNtUVKeeOD/CUC3xvtf23iPygTvDH8iFWU1VUkmHVKW
	| mdYlNaZazyH/lLgI+fIc6e5PVjVsU0hyMwIDAQABoyQwIjATBgNVHSUEDDAKBggr
	| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBAE5qk6HdlhFA
	| POtTPMlselPNXR8N9OjjXj4rU+CWNy0n5zeyOUZMmUckpjinUP+YlsqD0/SuQ0Y8
	| dJXyJl2OaBftzBD+Q6DpP4C4NYnXWje6TtGzr/ziw/u1ca2hpK4T62IRfjhjQBGy
	| +vL7mkfxMvsxdMBJFXrTkxzqIKOUoHILo0x2jTia3JaOaggfwks5qBimUp8QWV3D
	| RX1Epk2UmNOfgJryjnMWtrwwF5tYHIPfiadGjuOAfoaCIJVVlYra3LQ+bA8SzVqx
	| TtrRLxq3N5VsAMqCF7nMMYI1deie2nEMGwFqoDZMcKw+9R0bpG5DcDpHYCfzDh9l
	| L4EdHs5bOwo=
	|_-----END CERTIFICATE-----
	|_ssl-date: 2021-05-13T12:43:33+00:00; +1m18s from scanner time.
	Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

	Host script results:
	|_clock-skew: mean: 1m17s, deviation: 0s, median: 1m17s


80/Http is windows server IIS 10.0

/retro dir found this using wordpress 5.2.1

while looking into retra we got user pass

wade:parzival

then connect with rdp

	xfreerdp /u:wade /v:10.10.53.48:3389

we got user.txt

### Privsec

In windows desktop has chrome just open it and checking history we got **CVE-2017-0213**

Download here! https://github.com/WindowsExploits/Exploits/blob/master/CVE-2017-0213/Readme.md

and send to your victim machine then run

	./CVE-2017-0213_x64.exe

you got root!