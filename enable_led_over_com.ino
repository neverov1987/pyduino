
int datafromUser=0;
int status_1='0';
int status_2='0';
int status_3='0';
int status_4='0';
char status_list[4];
void setup() {
  // put your setup code here, to run once:
  pinMode( LED_BUILTIN , OUTPUT );
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(flag);
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }
       
  if(datafromUser == '1')
  {
    digitalWrite( LED_BUILTIN , HIGH );
    status_1='1';
  }
  else if(datafromUser == '0')
  {
    digitalWrite( LED_BUILTIN, LOW);
    status_1='0';
  }
    else if(datafromUser == '2')
  {
    status_2='1';
  }
     else if(datafromUser == '3')
  {
    status_2='0';
  }
    else if(datafromUser == '9')
  {
    status_list[0]=status_1;
    status_list[1]=status_2;
    status_list[2]=status_3;
    status_list[3]=status_4;
    Serial.println(status_list);
    delay(1000);
  }

}
