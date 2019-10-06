import socket
import threading
import sys
import pickle 

class Cliente():
	"""docstring for Cliente"""
	def __init__(self, host = "localhost", port = 7003):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host),int(port)))
		msg_recv = threading.Thread(target = self.msg_recv)
		msg_recv.daemon = True
		msg_recv.start()
		while True:
			msg = input('->')
			if msg != 'salir':
				self.send_msg(msg)
			else:
				self.sock.close()
				sys.exit()
	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1028)
				if data:
					data = pickle.loads(data)
					print(data)
			except:
				pass
	def send_msg(self,msg):
		try:
			self.sock.send(pickle.dumps(msg))
		except:
			print('error')	
