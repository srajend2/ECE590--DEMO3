import socket, binascii, time, serial, os, sys, tty, termios, math

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
turn_init=10
gripper_init=10

#initializing the servos to the init position
link1=link1_init
link2=link2_init
turn=turn_init
gripper=gripper_init

#defining initial position of the end effector 
x1_init=5.0
y1_init=10.0
z1_init=0.0
#defining maximum range of the end effector
x1_max=35.0
x1_min=-35.0
y1_max=30.0
z1_max=30.0
#initializing the end effector to initial position
x1=x1_init
y1=y1_init
z1=z1_init
#defining lengths of the links
l1=0.0
l2=25.0
l3=25.0

#function to format sending data
def conv(t,K):
        st1 = str(K)
        st2 = str(t).zfill(3)
        str1=st1+"/"+st2
        return str1

#calculating inverse kinematics
def convtheta(x,y,z):
	eqn1=abs(pow(x,2))+abs(pow(y,2))+abs(pow(l2,2))-abs(pow(l3,2))+abs(pow((z-l1),2))
	eqn2=abs(pow(x,2))+abs(pow(y,2))+abs(pow((z-l1),2))	
	eqn3=abs(pow(x,2))+abs(pow(y,2))-abs(pow(l2,2))-abs(pow(l3,2))+abs(pow((z-l1),2))
	link1_theta = math.degrees(math.acos((eqn1)/(2.0*l2*math.sqrt(eqn2)))) + math.degrees(math.atan2((z-l1),(math.sqrt(eqn2))))
	turn_theta = math.degrees(math.atan2((-x),y))
	link2_theta = math.degrees(math.acos((eqn3)/(2.0*l2*l3)))
	link1_theta=90.0-link1_theta
	link2_theta=180.0-link2_theta
	turn_theta=180.0+turn_theta-80
	val1=int(link1_theta)
	val2=int(link2_theta)
	val3=int(turn_theta)
	slink1_theta = str(val1).zfill(3)
	slink2_theta = str(val2).zfill(3)
	sturn_theta = str(val3).zfill(3)
	ret_x = str(x).zfill(2)
	ret_y = str(y).zfill(2)
	return_theta_prt = ret_x+"/"+ret_y+"/"+slink1_theta+"/"+slink2_theta+"/"+sturn_theta
	print return_theta_prt
	return_theta = "1"+"/"+slink1_theta+"/"+"2"+"/"+slink2_theta+"/"+"4"+"/"+sturn_theta
	return return_theta
	
while True:
	tty.setraw(sys.stdin.fileno()) #raw input
	ch = sys.stdin.read(1)         #store the read input character
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        #Keys 8 and 5 are used to increase and decrease the values of
	# 'y' value along Y axis (in steps of 0.5 centimeter) respectively
	if "8" in ch:
	    if((y1>=y1_init) and (y1<y1_max)):
		y1=y1+0.5
		theta_total=convtheta(x1,y1,z1)
                sock.sendto(theta_total, (IP,PORT))
		print theta_total
	if "5" in ch:
	    if((y1>y1_init) and (y1<=y1_max)):
		y1=y1-0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

        #Keys 6 and 4 are used to increase and decrease the values of
	# 'x' value along X axis (in steps of 0.5 centimeter) respectively
	if "4" in ch:
	    if((x1>x1_min) and (x1<=x1_max)):
		x1=x1-0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

	if "6" in ch:
	    if((x1>=x1_min) and (x1<x1_max)):
		x1=x1+0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

        #Keys w and s are used to increase and decrease the values of
	# 'y' value along Y axis (in steps of 0.5 centimeter) respectively
	if "s" in ch:
	    if((z1>z1_init) and (z1<=z1_max)):
		z1=z1-0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

	if "w" in ch:
	    if((z1>=z1_init) and (z1<z1_max)):
		z1=z1+0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

	#Keys e and d are used to close and release the gripper
	if "e" in ch:
	    if((z1>z1_init) and (z1<=z1_max)):
		z1=z1-0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total

	if "d" in ch:
	    if((z1>=z1_init) and (z1<z1_max)):
		z1=z1+0.5
		theta_total=convtheta(x1,y1,z1)
		sock.sendto(theta_total, (IP,PORT))
		print theta_total


	if "i" in ch:
		x1=x1_init
		y1=y1_init
		z1=z1_init		
		init_tx_value=convtheta(x1,y1,z1)
		print init_tx_value
		sock.sendto(init_tx_value, (IP,PORT))

	if ch in "c":
		break

