import socket
import ssl

target_host = "0.0.0.0"
target_port = 4444

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS
ssl_client = ssl.wrap_socket(client)

# Connect to the server
ssl_client.connect((target_host, target_port))

# Send some data (HTTP GET request)
request = b"GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n"
ssl_client.send(request)

# Receive and decode data
response = ssl_client.recv(4096)
decoded_response = response.decode("utf-8")

print(decoded_response)
