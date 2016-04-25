#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#define STEP_DEGREE 0.29296875
#define ID1  100 //link1
#define ID2 40  // link2
#define ID3 10  // centre
#define ID4 30  // gripper 
#define LOAD 41
Dynamixel Dxl(DXL_BUS_SERIAL1); 

int pos;
int capture=0;
int motpostest=80;

void setup() 
{
  
Dxl.begin(3);  
  Dxl.setPacketType(DXL_PACKET_TYPE2);
  SerialUSB.attachInterrupt(MOTOR_POS); 
  Dxl.wheelMode(ID2);
  Dxl.goalSpeed(ID2, 50);  
  delay(20);
  Dxl.maxTorque(ID2,1020); 
  delay(20);
  Dxl.jointMode(ID2);
  Dxl.wheelMode(ID1);
  delay(20);
  Dxl.goalSpeed(ID1, 50);  
  delay(20);
  Dxl.maxTorque(ID1,1020); 
  delay(20);
  Dxl.jointMode(ID1);
  Dxl.wheelMode(ID3);
  delay(20);
  Dxl.goalSpeed(ID3, 50);  
  delay(20);
  Dxl.maxTorque(ID3,1020); 
  delay(20);
  Dxl.jointMode(ID3);
  Dxl.wheelMode(ID4);
  delay(20);
  Dxl.goalSpeed(ID4, 50);  
  delay(20);
  Dxl.maxTorque(ID4,1020); 
  delay(20);
  Dxl.jointMode(ID4);
  motpostest=80;
  Dxl.goalPosition(ID4, (motpostest/STEP_DEGREE));
}

void loop() 
{
  //delay(6000);              
  //delay(6000); 
    if(capture==1)
    {  
      pos = Dxl.readWord(ID4, LOAD);
      SerialUSB.println(pos);
    while(!((pos>=170)&&(pos<=800)))
      {  
      motpostest=motpostest-2;
       Dxl.goalPosition(ID4, (motpostest/STEP_DEGREE));
       delay(500);
       pos = Dxl.readWord(ID4, LOAD);
      SerialUSB.println(pos); 
      if (motpostest<=10)
        {pos=175;}
        
      } 
   capture=0;
  }
}
void MOTOR_POS(byte* buffer, byte nCount)
{
  Dxl.goalSpeed(ID2, 50);  
  Dxl.goalSpeed(ID1, 50); 
  Dxl.goalSpeed(ID3, 50);  
  Dxl.goalSpeed(ID4, 50); 
  int Key1 = (buffer[0]-48);
  int Key2 = (buffer[6]-48);
  int Key3 = (buffer[12]-48);
  int Key4 = (buffer[18]-48);
  int M1 = (((buffer[2]-48)*100)+((buffer[3]-48)*10)+(buffer[4]-48));
  int M2 = (((buffer[8]-48)*100)+((buffer[9]-48)*10)+(buffer[10]-48));
  int M3 = (((buffer[14]-48)*100)+((buffer[15]-48)*10)+(buffer[16]-48));
  int M4 = (((buffer[20]-48)*100)+((buffer[21]-48)*10)+(buffer[22]-48));
  Dxl.goalPosition(ID1, (M1/STEP_DEGREE));
  Dxl.goalPosition(ID2, (M2/STEP_DEGREE));
  Dxl.goalPosition(ID3, (M3/STEP_DEGREE));  
  if(Key4==4)
  {
                SerialUSB.println(Key4);
                SerialUSB.println(M4);
                if(M4==80)
                {
                Dxl.goalPosition(ID4, (M4/STEP_DEGREE));
                capture=0;
                }
                if(M4==20)
                {
                capture=1;
                }                
  }
  SerialUSB.println("Start");
  SerialUSB.println(Key1);
  SerialUSB.println(M1);
  SerialUSB.println(Key2);
  SerialUSB.println(M2);
  SerialUSB.println(Key3);
  SerialUSB.println(M3);
  SerialUSB.println(Key4);
  SerialUSB.println(M4);
  SerialUSB.println("End");
}

