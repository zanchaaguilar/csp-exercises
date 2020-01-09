#import the socket module
import socket

#socket method to create the socket client
s=socket.socket(socket.AF.INET, socket.SOCK_STREAM)
#connect client to server
#same port number to the server
s.connect((socket.gethostname(), 1025))

#accept any info that is send form thr server
complete_info = ''

#while the connection is true
while True:

	#save the message receiving into msg and specify bytes as a parameter
	msg=s.recv(7) 

	#msg is less than equal to zero it will break
	if len(msg)<=0:
		break
	#if not complete_info is printed in 7 bytes per transfer
	complete_info += msg.decode("utf-8")

	print(complete_info)