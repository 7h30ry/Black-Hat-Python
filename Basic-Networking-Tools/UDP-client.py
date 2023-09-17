import socket
import ssl

target_host = 'www.google.com'
target_port = 443

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish an SSL/TLS connection
ssl_context = ssl.create_default_context()
ssl_client = ssl_context.wrap_socket(client, server_hostname=target_host)

# Connect to the server
ssl_client.connect((target_host, target_port))

# Send some data (HTTP GET request)
request = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
ssl_client.send(request)

# Receive and decode data
response = ssl_client.recv(4096)
decoded_response = response.decode("utf-8")

print(decoded_response)
