import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
s = [0]
while True:
        
	ser.write('1')
      
        #s[0] = str(int (ser.readline(), 16))
        #print s[0]

        #print(ser.readline())

        print("Made it to the first serial \n")

        time.sleep(2)

        print("Made it to the second serial \n")
        
        ser.write('2')

        time.sleep(2)

	#print "Made it to here lol"
	#read_serial=ser.readline()
	#s[0] = str(int (ser.readline(),16))
	#print s[0]
	#print read_serial






