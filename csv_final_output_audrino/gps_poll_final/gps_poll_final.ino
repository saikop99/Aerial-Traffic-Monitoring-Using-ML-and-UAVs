void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(P1_4,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly: 
  int sensorValue=analogRead(P1_4);
  Serial.write("Hello World");
  delay(1000);
  Serial.print(sensorValue);
  Serial.println();
  delay(200);
}
