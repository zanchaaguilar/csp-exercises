import socket
import pickle

#specify the header size
a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2133))

while True:
	#comlete info received from the server to the client in bytes
	#specify b with a empty string
	complete_info = b''
	
	#specify the msg received from the server to the client is true
	rec_msg = True

	while True:
		#received 16bytes per transfer
		mymsg = s.recv(16)

		#if the msg received is complete then the msg received var will set to false	
		if rec_msg
			print(f"The length of message = {mymsg[:a]}")
			x = int (mymsg[:a])
			rec_msg = False
		#if not false the msg will be incremented and the next chunk of msg will be received in 16bytes per transfer
		complete_info += mymsg
		#if complete info received is equal to len of the msg on the server then print
		if len(complete_info)-a == x:
			print("Received the complete info")
			print(complete_info[a:])
			
			#pass complete info that received from the server to the client
			m = pickle.loads(complete_info[a:])
			#print msg that received from the server to the client
			print(m)
			rec_msg = True
			complete_info = b''
	print(complete_info)