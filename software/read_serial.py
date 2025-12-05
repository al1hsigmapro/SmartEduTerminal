import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
    if ser.in_waiting:
        data = ser.readline().decode().strip()
        print(data)
