import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

#This is our client handling socket
def handle_client(client_socket):
    #print out what the client says
    client_socket.send(b"ACK!")

    client_socket.close()

while True:
    client,addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    #spin our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()