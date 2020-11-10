import serial
import os

def DataInladen():

    # os.remove("analog-data.csv")      # clear previous csv file
    arduino_port = "COM3"
    baud = 19200
    filename = "analog-data.csv"
    samples = 9                        # max 10 lines in file

    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    # file = open(filename, "w")
    print("Created file")
    line = 0

    while line <= samples:              # replace (line <= samples) to True, if u want infinite writing to csv file

        print("Line " + str(line) + ": writing...")

        getData=str(ser.readline().decode('ASCII'))
        data = getData
        print(data)

        file = open(filename, "a", newline='')
        file.write(data)

        line = line+1
    print("Data collection Completed")

DataInladen()