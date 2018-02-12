#!/usr/bin/python
import socket
import time
import re

filename = "zcta.csv"
geoid = 1
population = 2
housing = 3
land = 4
water = 5
latitude = 8
longitude = 9

def getZip(message):
    return re.findall(r'[0-9]{5}',message)

def getData(column, zipcode, message):
    for line in open(filename, 'r'):
        if re.search("^" + zipcode, line):
            csvData = line.split(",")
    return csvData[column -1]


def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(('c1.easyctf.com',12483))
    time.sleep(5)

    message = s.recv(1024)

    while not "easyctf" in message:

        print(message)
        zipcode = getZip(message)

        if "water" in message:
            column = water
        elif "latitude" in message:
            column = latitude
        elif "longitude" in message:
            column = longitude
        elif "land" in message:
            column = land

        data = getData(column, zipcode[0], message)
        print (data)

        s.send(data + "\r\n")
        message = s.recv(1024)
        print (message)

    s.close()

if __name__ == '__main__':
    main()
