import socket
import threading
import time

host = '127.0.0.1'
port = 5051
peers = ['5051'] # add the peers that sent messages to the client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create a socket
client = {}
temp = {}
i = 1
def receive_messages():
    global i  # Access the global variable i
    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode()
        # if the peer send "CONNECT" to the server then we can add it to the peer array
        if message == "CONNECT":
            peers.append(str(addr[1]))
            broadcast()
        # if the peer send  to the server then we can add it to the peer array
        else:
            current_time = time.strftime('%H:%M:%S', time.localtime())
            words = message.split()
            Message = " ".join(words[2:])  # Join remaining words into Message
            # Store client details in a tuple and add to client dictionary
            client[addr[1]] = (words[0], words[1], current_time, Message)
            # Store address in temp list using current index i
            temp[i] = addr[1]
            # Print received message information
            print(f'{i} - Received message from {words[0]} {words[1]} at {current_time}')
            # Increment i to prepare for the next message
            i += 1

def broadcast():
    peersMsg = ",".join(peers)  # Join peers into a comma-separated string
    for peer in peers:
        if int(peer) != port: # do not send the port to the server
            sock.sendto(peersMsg.encode(), (host, int(peer))) # send the new peer port to all the peers so that they can send it to the peers

if __name__ == "__main__":
    sock.bind((host, port))
    print(f"Server listening on {host}:{port}")
    # Start a thread to continuously receive messages
    threading.Thread(target=receive_messages).start()
    print('Peer first name last name')

    while True:
        if i == 3:
            option = input("Enter an option: ")
            if int(option) in range(1, i + 1):
                first_name, second_name, received_time, message = client[temp[int(option)]]
                print("Your message is:", message)
            else:
                print("Invalid option")

