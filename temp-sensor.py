import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0, 0)

lightChannel = 1
sleepTime = 1

def getReading(channel):
    rawData = spi.xfer([1, (8 + channel) << 4, 0])
    processedData = ((rawData[1]&3) << 8) + rawData[2]
    return processedData

def convertVoltage(bitValue, decimalPlaces=2):
    voltage = (bitValue * 3.3) / float(1023)
    voltage = round(voltage, decimalPlaces)
    return voltage

while True:
    lightData = getReading(lightChannel)
    lightVoltage = convertVoltage(lightData)
    print("Light bitValue = {}; Voltage = {} V".format(lightData, lightVoltage))
    sleep(sleepTime)    
