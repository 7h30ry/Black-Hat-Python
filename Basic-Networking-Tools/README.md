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
