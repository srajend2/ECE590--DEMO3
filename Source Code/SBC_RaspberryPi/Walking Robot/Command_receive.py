import socket, serial

UDP_IP = "192.168.1.20"
UDP_PORT = 5005

DEVICE = '/dev/ttyACM0'
BAUD = 9600
ser = serial.Serial(DEVICE,BAUD)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
        data, addr = sock.recvfrom(1024) # buffer size = 1024 bytes
        print "received message:", data
	ser.write(data)


