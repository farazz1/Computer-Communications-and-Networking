import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("udp_log.txt", "a") as log_file:
    lost_packets = 0

    for i in range(100):  # Send 100 messages
        message = f"Message {i+1}"
        start_time = time.time()  # Start timer
        client_socket.sendto(message.encode(), ("localhost", 12346))  # Send message

        try:
            client_socket.settimeout(0.5)  # Wait for a response with timeout
            data, _ = client_socket.recvfrom(1024)  # Receive response
            end_time = time.time()  # End timer
            round_trip_time = end_time - start_time  # Calculate RTT
            print(f"Server: {data.decode()}")
            log_file.write(f"Sent: {message}, RTT: {round_trip_time:.6f} sec\n")
        except socket.timeout:
            lost_packets += 1  # Count lost packets
            print(f"Packet lost: {message}")
            log_file.write(f"Lost: {message}\n")

    log_file.write(f"\nTotal packets lost: {lost_packets}/100\n")

client_socket.close()
