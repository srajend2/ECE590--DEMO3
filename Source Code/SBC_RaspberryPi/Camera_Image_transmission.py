import sys, os, socket, binascii, time, picamera
from PIL import Image

IP2 = "192.168.1.10"
PORT2 = 5006

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
try:
  while(True):
      with picamera.PiCamera() as cam:
        cam.resolution=(150,120)                          #Specifying smaller resolution for quick transmission
        cam.start_preview()                               #Start Pi camera
	cam.vflip = True
        cam.hflip = True
        image=cam.capture('Desktop/piframe.bmp')          #Save image in bitmap format
        cam.stop_preview()
	imgframe = 'Desktop/piframe.bmp'                  #Assign image path to variable
	imgframe1 = Image.open(imgframe).convert('L')     #Convert image to grayscale
	imgframe1.save('Desktop/piconvframe.bmp')         #Save grayscale image in bitmap format
	imgframe2 = 'Desktop/piconvframe.bmp'             #Assign image path to variable
        imgsize = os.path.getsize(imgframe2)              #Get the size of that image file
	with open(imgframe2, 'rb') as f:                  #Read the image in binary format and store in content as one single string
             content = f.read()
	imgtext = binascii.hexlify(content)               #Convert the string from binary to hexadecimal format
	print 'transmitting'
	sock.sendto(imgtext, (IP2,PORT2))                 #Send the converted string via socket (UDP)

except KeyboardInterrupt:
	print 'exiting program'
	sock.close()                                      #Close socket
	cam.stop_preview()                                #Stop camera
