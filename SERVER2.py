#import the socket and pickle module
import socket
import pickle

#header specifying a
a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2133))	#binding tuple
s.listen(5)

while True:
	clt, adr=s.accept()
	print(f"Connection to {adr} established")

	#declares m dictionary 
	m={1:"Client", 2:"Server"}

	#dumps method serialized object of dictionary
	mymsg = pickle.dumps(m)		#the msg we want to print later
	#incrimenting the mymsg
	mymsg = bytes(f'{len(mymsg) :<{a}}',"utf=8") + mymsg
	#sending the mymsg to the client using the send method
	clt.send(mymsg)