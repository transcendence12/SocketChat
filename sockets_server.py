import socket


HOST_IP = "127.0.0.1"
PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADOR, 1) - if server dont want rerun on Windows
# bind() - accepts tuple
s.bind((HOST_IP, PORT))
s.listen()

print(f"Connection on {HOST_IP}, on port {PORT}...")

connection_socket, client_address = s.accept()

print(f"Connection {client_address}")

while True:
    text_send = input("You: ")
    connection_socket.sendall(text_send.encode())
    data_received = connection_socket.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print("Message: ", data_received.decode())

s.close()
connection_socket.close()