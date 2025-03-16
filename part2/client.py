import socket
import threading
import time

host = '127.0.0.1'
peers = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client = {}
temp = {}
server_port = 5051
i = 1


def receive_messages():
	global i  # Access the global variable i
	while True:
		data, addr = sock.recvfrom(1024)
		message = data.decode()
		if addr[1] == server_port:
			processServerMsg(message)

		else:
			current_time = time.strftime('%H:%M:%S', time.localtime())
			words = message.split()
			Message = " ".join(words[2:])  # Join remaining words into Message
			# Store client details in a tuple and add to client dictionary
			# Store address in temp list using current index i
			client[addr[1]] = (words[0], words[1], current_time, Message)
			temp[i] = addr[1]

			# Increment i to prepare for the next message
			i += 1


def broadcast(message):
		global peers

		for peer in peers:
				if peer != port:  # Don't send to myself
						sock.sendto(message.encode(), (host, peer))

def talkToServer():
		sock.sendto("CONNECT".encode(), (host, server_port))

def processServerMsg(message):
		global peers
		newPeers = message.split(",")
		peers = []
		for newPeer in newPeers:
				if newPeer == "":
						continue
				peers.append(int(newPeer))

if __name__ == "__main__":
		# Bind the socket to an available port on the host
		sock.bind((host, 0))
		port = sock.getsockname()[1]
		print(f"Peer listening on {host}:{port}")
		# Start a thread to continuously receive messages
		talkToServer()
		threading.Thread(target=receive_messages).start()


		# Get user input for first name, last name, and message
		firstName = input("Enter your first name: ")
		lastName = input("Enter your last name: ")
		message = input("Enter message: ")
		# Construct the message to be broadcasted
		Message = f'{firstName} {lastName} {message}'
		# Broadcast the message to all peers
		broadcast(Message)

		while i != 2:
			time.sleep(1)  # Wait for 1 second before checking again
		print('Peer first name last name')
		for j in temp:
			first_name, second_name, received_time, message = client[temp[j]]
			print(f'{j} - Received message from {first_name} {second_name} at {received_time}')
		while True:
			option = input("Enter an option: ")
			if int(option) in range(1, i + 1):
				first_name, second_name, received_time, message = client[temp[int(option)]]
				print("Your message is:", message)
			else:
				print("Invalid option")



