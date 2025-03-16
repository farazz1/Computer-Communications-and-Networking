import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12346))  # UDP server on port 12346

print("UDP Server is listening...")

with open("udp_log.txt", "w") as log_file:
    for _ in range(100):  # Process 100 messages
        data, addr = server_socket.recvfrom(1024)  # Receive data
        message = data.decode()

        if random.random() > 0.2:  # Simulating packet loss (20% chance of loss)
            print(f"Received: {message}")
            log_file.write(f"Received: {message}\n")
            server_socket.sendto(f"Received: {message}".encode(), addr)  # Respond
        else:
            print(f"Dropped packet: {message}")
            log_file.write(f"Dropped: {message}\n")

server_socket.close()
