TCP vs. UDP Client-Server Comparison

How to Run the Programs

1️⃣ Running the TCP Client-Server
1. Open a terminal and start the TCP server:
   python tcp_server.py
   - The server will start and wait for connections.

2. Open another terminal and run the TCP client:
   python tcp_client.py
   - The client will send 100 messages to the server and receive responses.
   - The latency (round-trip time) will be logged in tcp_log.txt.

2️⃣ Running the UDP Client-Server
1. Open a terminal and start the UDP server:
   python udp_server.py
   - The server will start and wait for incoming UDP messages.

2. Open another terminal and run the UDP client:
   python udp_client.py
   - The client will send 100 messages to the server.
   - Some messages will be lost (simulated packet loss of ~20%).
   - The results will be logged in udp_log.txt.

Expected Outputs
- TCP: All 100 messages will be received, with measured round-trip times (RTT) recorded in tcp_log.txt.
- UDP: Some messages will be lost due to simulated packet loss (~20%), with results recorded in udp_log.txt.
- The terminal will display message exchanges between client and server.

Example TCP Log Output (tcp_log.txt):
Sent: Message 1, RTT: 0.012345 sec
Sent: Message 2, RTT: 0.011234 sec
...
Sent: Message 100, RTT: 0.009876 sec

Example UDP Log Output (udp_log.txt):
Sent: Message 1, RTT: 0.005678 sec
Sent: Message 2, RTT: 0.006432 sec
Lost: Message 3
Sent: Message 4, RTT: 0.004321 sec
...
Total packets lost: 18/100

Observations: TCP vs. UDP Behavior

1️⃣ Latency Comparison
- TCP has higher latency due to its connection-oriented nature and acknowledgment mechanism.
- UDP has lower latency because it sends packets without waiting for a response.

2️⃣ Reliability and Packet Loss
- TCP guarantees reliable delivery of all packets with retransmission.
- UDP can drop packets, making it less reliable but faster.

3️⃣ Throughput Analysis
- TCP is slower due to acknowledgments and retransmissions.
- UDP is faster but sacrifices reliability.

4️⃣ Use Cases
- TCP is used for reliable communication (e.g., HTTP, file transfers, emails).
- UDP is used for speed-sensitive applications (e.g., VoIP, video streaming, online gaming).

How This Was Accomplished
To understand and implement TCP and UDP client-server communication, the following resources were used:
- Python Socket Programming: https://docs.python.org/3/library/socket.html
- Real-world TCP vs. UDP Use Cases: https://www.cloudflare.com/learning/ddos/glossary/tcp-udp/
- Networking basics and packet transmission concepts from online tutorials and lecture notes.

This project demonstrates the fundamental differences between TCP and UDP through practical coding exercises and performance analysis.

