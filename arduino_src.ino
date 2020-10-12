// Определение стартовых значений
int datafromUser=0;
int status_1='0';
int status_2='0';
int status_3='0';
int status_4='0';
char status_list[4]; // назанчение массива для передачи информации по запросу статуса
void setup() {
  // put your setup code here, to run once:
  pinMode( LED_BUILTIN , OUTPUT ); //Назанчение пина светодиода (внутренний светодиод)
  Serial.begin(9600); // Назначение скорости порта
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) //Проверка, что буфер передачи досутпен
  {
    datafromUser=Serial.read(); //Чтение буфера
  }
 // Начало. Определение и выполнение задания 
  if(datafromUser == '1') 
  {
    digitalWrite( LED_BUILTIN , HIGH ); //Включение диода
    status_1='1'; //Назначение флага включенного диода
  }
  else if(datafromUser == '0') 
  {
    digitalWrite( LED_BUILTIN, LOW); //Выключение диода
    status_1='0'; //Назначение флага выключенного диода
  }
  else if(datafromUser == '2') //Включение реле 1
  {
    status_2='1'; //Назаначение флага включенного реле 1
  }
  else if(datafromUser == '3') //Выключение реле 1
  {
    status_2='0'; // Назначение флага выключенного реле 1
  }
  else if(datafromUser == '9') //Получение команды отправки сатистики
  {
 //Сборка массива для отправки статистики
    status_list[0]=status_1;
    status_list[1]=status_2;
    status_list[2]=status_3;
    status_list[3]=status_4;
 //Конец сборки массива для отправки статистики
    Serial.println(status_list); //Отправка массива статистики в порт
    delay(1000);                 //Ожидание (нужно для корректной отправки, иначе данные дублируются и массив отдается не корректно)
  }

}
