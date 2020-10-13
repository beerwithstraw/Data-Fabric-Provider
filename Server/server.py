import socket
import threading
import os

def RecvFile (sock,addr,docName):
	sock.send(docName)
	resp = sock.recv(1024)
	if resp[:4] == 'OKAY':
		print "\tMessage sent to client <ip: " +str(addr)+">"
	filename = sock.recv(1024)
	if os.path.isfile(filename):
		sock.send("EXISTS "+ str(os.path.getsize(filename)))
		userResponse = sock.recv(1024)
		if userResponse[:2] == 'OK':
			with open("Clients.txt", "a") as myfile:
				myfile.write("Client: "+ str(addr)+" downloaded the file '"+docName+"'\n")
			print "\tClient: "+str(addr)+" disconnected! "
			with open(filename, 'rb') as f:
				bytesToSend = f.read(1024)
 				sock.send(bytesToSend)
				while bytesToSend != "":
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)
		else:
			with open("Clients.txt", "a") as myfile:
				myfile.write("Client: "+ str(addr)+" did not download the file\n")
			print "\tClient: "+str(addr)+" disconnected! "
	else:
		sock.send("Error!")

	sock.close()

def Main():

	port = 5001
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("localhost", port))
	server_socket.listen(10)
	print "\33[32m \t\t\t\tSERVER WORKING \33[0m"
	docName = raw_input("Enter filename you wish to distribute: ")
	print "Waiting for connection..."
	while True:

			c,addr = server_socket.accept()
			print "Client connected <ip: "+str(addr)+" >"
			t = threading.Thread(target=RecvFile, args=(c,addr,docName))
			t.start()

				
	server_socket.close()

if __name__=='__main__':
	Main()
