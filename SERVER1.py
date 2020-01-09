#socket module
import socket

#create the socket using the socket method
#AF.INET is address from the internet requires host and port number
#socket.SOCK_STREAM is for creating tcp protocols
s=socket.socket(socket.AF.INET, socket.SOCK_STREAM)

#bind function accepts 2 parameters as a tuple wc is a host and a port num
# server as well as the client are on the same computer or device and specify a port number
# bind method for it to bind to the client
s.bind((socket.gethostname(), 1025))

#
s.listen(5)

#while the connection is true
while True:
	#server accept the client server and the address
	client, adrs=s.accept()
	
	#if received print
	print(f"Connection to {adrs} establish")
	#if the conn is establish pass message from the server to client
	#it specify bytes so it use utf-8
	client.send(bytes("Socket Programming in Python, "utf-8"))
	client.close()