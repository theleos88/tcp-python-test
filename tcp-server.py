import socket
ADDRESS = ''
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen(1)

client, addressClient = server.accept()
print ('Connected from ', addressClient)

data = client.recv(1024)
if not data:
	print ('RECV error.')
else:
	print ('DATA ||  ' + str(data))
	response = "MIRRORING - " + str(data[::-1])
	print ('RESPONSE || ' + response)
	n = client.send(bytes(response, encoding='utf-8'))
	if (n != len(response)):
		print ('RESP error.')
	else:
		print ('RESP sent.')

	print ('CLOSING CONNECTION.')
	client.close()
	print ('STOPPING SERVER.')
	server.close()
