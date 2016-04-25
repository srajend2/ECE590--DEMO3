import socket, binascii, time, serial, os, sys, tty, termios

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
IP = "192.168.1.20"
PORT = 5005

#termios is used for POSIX input/output control
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

#initial position values of servos
link1_init=10
link2_init=20
turn_init=40
gripper_init=10

#initializing the servos to the init position
link1=link1_init
link2=link2_init
turn=turn_init
gripper=gripper_init

#function to format sending data
def conv(t,K):
        st1 = str(K)
        st2 = str(t).zfill(3)
        str1=st1+"/"+st2
        return str1

while True:
	tty.setraw(sys.stdin.fileno())  #raw input
	ch = sys.stdin.read(1)          #store the read input character
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        #Keys 7 and 4 used to control link1
	if "7" in ch:
                link1=link1+1
                str2=conv(link1,'1')
               # ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2

	if "4" in ch:
           if(link1>=link1_init+1):
                link1=link1-1
                str2=conv(link1,'1')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
        	print str2
        #Keys 8 and 5 used to control link2
	if "8" in ch:
                link2=link2+1;
                str2=conv(link2,'2')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2

	if "5" in ch:
           if(link2>=link2_init+1):
                link2=link2-1
                str2=conv(link2,'2')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2
        #Keys 9 and 6 used to control gripper
	if "9" in ch:
                gripper=gripper+1
                str2=conv(gripper,'3')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2

	if "6" in ch:
           if(gripper>=gripper_init+1):
                gripper=gripper-1
                str2=conv(gripper,'3')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2
        #Keys 1 and 3 used to control turn
	if "1" in ch:
                turn=turn+1
                str2=conv(turn,'4')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2

	if "3" in ch:
           if(turn>=turn_init+1):
                turn=turn-1
                str2=conv(turn,'4')
                #ser.write(str2)
		sock.sendto(str2, (IP,PORT))
		print str2

	if ch in "c":
		break

