import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))  # Connect to server

with open("tcp_log.txt", "a") as log_file:
    for i in range(100):  # Send 100 messages
        message = f"Message {i+1}"
        start_time = time.time()  # Start timer
        client_socket.sendall(message.encode())  # Send message
        response = client_socket.recv(1024).decode()  # Receive response
        end_time = time.time()  # End timer
        round_trip_time = end_time - start_time  # Calculate RTT

        print(f"Server: {response}")
        log_file.write(f"Sent: {message}, RTT: {round_trip_time:.6f} sec\n")

client_socket.close()
