import socket, time, re, os, binascii, sys, pygame

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
IP = "192.168.1.10"
PORT = 5006

sock.bind((IP, PORT))

try:
     while(True):
	receivedimghex = " "
 	data, addr = sock.recvfrom(40000)   #receiving datagram of 40000 bytes
	receivedimghex = receivedimghex + data
	reformatimg = receivedimghex[1:]     #Read from the second character onwards
	actualimg = binascii.unhexlify(data) #convert hexadecimal representation to binary format
	fo = open("Desktop/rcvdimg.bmp",'wb') #open in write binary format
	fo.write(actualimg)                   #write the received image to the path
	fo.close()                            #close the file after write
	filename = "Desktop/rcvdimg.bmp"      
	img = Image.open(filename)   #at this point if there is a default image viewer
                                     #installed, the image will open, else it has to be
                                     #opened manually and the image would be updated as
                                     #the image is iteratively received
	img.show(command='fim')

except KeyboardInterrupt:
	print('End process')
	sock.close()


