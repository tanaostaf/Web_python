
import socket
from datetime import datetime 


address = ('localhost', 16789)
max_size = 1000

print('Starting the client at', datetime.now())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)
client.sendall(b'Hey!')
data = client.recv(max_size)

print('At', datetime.now(), client, 'someone replied', data)

client.close()



