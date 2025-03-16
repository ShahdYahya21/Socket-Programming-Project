## Socket Programming: Network Exploration, UDP Communication, and Web Server Implementation
### Part 1: Network Exploration

Basic network tools were defined: 
- `ping` (which tested network connectivity)
- `tracert` (which showed the route of data packets)
- `nslookup` (which queried DNS for domain name information)
- `telnet` (a protocol for remote access to another computer)

These tools were used to explore network connections and analyze the results (e.g., a website was pinged, and its location was determined based on the response). Wireshark was used to capture and examine DNS messages, which were essential for domain name resolution.

### Part 2: UDP Communication

A simple chat system was implemented using UDP sockets. 
- A server was created to listen on a specific port (5051), and client applications were developed to send messages to and receive messages from the server.
- Messages included the sender's first and last name and the message content.
- The server kept track of the last message received from each client.
- Clients were able to view the history of received messages.
- Broadcast addresses were used for sending messages to all peers on the network.

### Part 3: Web Server Implementation

A basic web server was built to listen on port 6060. 
- The server handled different types of HTTP requests.
- HTML files, CSS files, and image files (.png and .jpg) were served by the server.
- Requests were redirected to other websites when necessary.
- If a requested file was not found, a 404 error page was returned by the server.
- The HTTP requests received were printed by the server.
- "Entity Tag Cache Validators" in the HTTP protocol were also understood and implemented.
