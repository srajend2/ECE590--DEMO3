#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#define STEP_DEGREE 0.29296875
#define ID1 100 //link1
#define ID2 40  // link2
#define ID3 10  // centre
#define ID4 30  // gripper 
Dynamixel Dxl(DXL_BUS_SERIAL1); 
void setup() 
{
  
Dxl.begin(3);  
  Dxl.setPacketType(DXL_PACKET_TYPE2);
  SerialUSB.attachInterrupt(MOTOR_POS); 
  Dxl.wheelMode(ID2);
  Dxl.goalSpeed(ID2, 50);  
  delay(20);
  Dxl.maxTorque(ID2,1020); // it has maxtorque
  delay(20);
  Dxl.jointMode(ID2);
  Dxl.wheelMode(ID1);
  delay(20);
  Dxl.goalSpeed(ID1, 50);  
  delay(20);
  Dxl.maxTorque(ID1,1020); // it has maxtorque
  delay(20);
  Dxl.jointMode(ID1);
  Dxl.wheelMode(ID3);
  delay(20);
  Dxl.goalSpeed(ID3, 50);  
  delay(20);
  Dxl.maxTorque(ID3,1020); // it has maxtorque
  delay(20);
  Dxl.jointMode(ID3);
  Dxl.wheelMode(ID4);
  delay(20);
  Dxl.goalSpeed(ID4, 50);  
  delay(20);
  Dxl.maxTorque(ID4,1020); // it has maxtorque 
  delay(20);
  Dxl.jointMode(ID4);
}

void loop() 
{
  //delay(6000);              
  //delay(6000); 
}
void MOTOR_POS(byte* buffer, byte nCount)
{
  Dxl.goalSpeed(ID2, 50);  
  Dxl.goalSpeed(ID1, 50); 
  Dxl.goalSpeed(ID3, 50);  
  Dxl.goalSpeed(ID4, 50); 
  int Key = (buffer[0]-48);
  int M1 = (((buffer[2]-48)*100)+((buffer[3]-48)*10)+(buffer[4]-48));
        if (Key==1)
        {
                SerialUSB.println(Key);
                SerialUSB.println(M1);
                Dxl.goalPosition(ID1, (M1/STEP_DEGREE));
        }
        if (Key==2)
        {
                SerialUSB.println(Key);
                SerialUSB.println(M1);
                Dxl.goalPosition(ID2, (M1/STEP_DEGREE));
        }
        if (Key==4)
        {
                SerialUSB.println(Key);
                SerialUSB.println(M1);
                Dxl.goalPosition(ID3, (M1/STEP_DEGREE));
        }
      if (Key==3)
      {
                SerialUSB.println(Key);
                SerialUSB.println(M1);
                Dxl.goalPosition(ID4, (M1/STEP_DEGREE));
      }
}           
