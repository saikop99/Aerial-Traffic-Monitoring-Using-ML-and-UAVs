import serial
import datetime
data_file = open("data.txt","w")
ser = serial.Serial('COM6',9600) #9600 Bodrate
for i in range (10):
    currentDT = str(datetime.datetime.now())
    x = []
    y = []
    x,y = currentDT.split(" ")
    se = ser.readline()[:-2]
    z = []
    se = se.decode('ascii','ignore') #Decoding to an intige
    z = str(se)
    data_file.write(x+","+y+","+z)
    data_file.write("\n")
	print(z+"\n)
ser.close()
data_file.close()
print("done")
