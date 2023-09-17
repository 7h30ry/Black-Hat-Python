# Basic Networking Tools
```
python netcat.py --help
```
## Example
Start a listener
```
python netcat.py -t 192.168.0.0 -p 5555 -l -c
```
Connect to it
```
python netcat.py -t 192.168.0.0 -p 5555
CTRL-D
<BHP:#> ls -la
```
We can run local commands and receive output
in return, as if we had logged in via SSH or were on the box locally.
We can perform the same setup on the Kali machine but have it
execute a single command using the -e 
```
python netcat.py -t 192.168.0.0 -p 5555 -l -e="cat
/etc/passwd"
```
```
python netcat.py -t 192.168.0.0 -p 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
```
We could also use netcat on the local machine:
```
nc 192.168.0.0 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
```

Finally, we could use the client to send out requests the good, old-
fashioned way:
```
 echo -ne "GET / HTTP/1.1\r\nHost: reachtim.com\r\n\r\n"
|python ./netcat.py -t reachtim.com -p 80

HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Mon, 18 May 2020 12:46:30 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: 229
Connection: keep-alive
Location: https://reachtim.com/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a
href="https://reachtim.com/">here</a>.</p>
</body></html>
```
