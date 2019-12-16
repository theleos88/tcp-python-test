import socket

HOST = '1.1.1.20'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print 'CONNECTING TO ' + HOST + ':' + str(PORT)

message = 'Hello, world'
print 'SEND || ' + message
n = client.send(message)
if (n != len(message)):
	print 'SEND Error'
else:
	print 'SEND Ok'

print 'RECV...'
data = client.recv(1024)
print 'DATA RECV || ', data
print 'DISCONNECT.'
client.close()

