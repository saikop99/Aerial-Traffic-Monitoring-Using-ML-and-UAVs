import serial

ser = serial.Serial('/dev/ttyACM0',9600) #9600 Bodrate
for i in range (10):
    se = ser.readline()[:-2]
    z = []
    se = se.decode('ascii','ignore') #Decoding to an intige
    z = str(se)
    print(z)
ser.close()
