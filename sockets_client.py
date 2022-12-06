import socket
import time


HOST_IP = "127.0.0.1"
PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connection on {HOST_IP}, on port {PORT}")
# funkcja blokująca więc print wyzej
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, PORT))
    except ConnectionRefusedError:
        print("Error: Cannot connect to the server. Reconnection...")
        time.sleep(4)
    else:
        print("Connection to server...")
        break

while True:
    data_received = s.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print("Message: ", data_received.decode())
    text_send = input("You: ")
    s.sendall(text_send.encode())

s.close()
