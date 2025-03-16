import socket
import time

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))  # Bind to localhost on port 12345
server_socket.listen(5)  # Listen for incoming connections

print("TCP Server is listening...")

conn, addr = server_socket.accept()  # Accept client connection
print(f"Connected to {addr}")

with open("tcp_log.txt", "w") as log_file:
    for _ in range(100):  # Receive 100 messages
        start_time = time.time()  # Start timer
        message = conn.recv(1024).decode()
        end_time = time.time()  # End timer
        round_trip_time = end_time - start_time  # Calculate RTT

        print(f"Received: {message}")
        log_file.write(f"{message}, RTT: {round_trip_time:.6f} sec\n")

        conn.sendall(f"Received: {message}".encode())  # Send response

conn.close()  # Close connection
server_socket.close()
