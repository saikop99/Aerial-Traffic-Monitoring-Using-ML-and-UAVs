#include <LiquidCrystal.h>
int sensorValue;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup(){  lcd.begin(16, 2);
Serial.begin(9600);                            // sets the serial port to 9600
 }
void loop(){sensorValue = analogRead(0);       // read analog input pin 0
Serial.print(sensorValue, DEC);               // prints the value read
Serial.println("");

delay(100);                                   // wait 100ms for next reading
}
