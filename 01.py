#!/usr/bin/python
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	print "Sending evil buffer...\n"
	s.connect(('192.168.0.145',110))
	data=s.recv(1024)
	print data
	
	s.send('USER yumingyuan\r\n')
	data=s.recv(1024)
	print data
	
	s.send('PASS test\r\n')
	data=s.recv(1024)
	print data
	s.close()
	print 'Connect Pop3 Done!'
except:
	print 'Could not connect to POP3!'
