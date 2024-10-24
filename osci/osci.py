import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#VDD-PIN 17 
#GND-PIN 9
#SCL-PIN 5
#SDA-PIN 3
 
#step 2 :- visit to the link of Adafruit ADC Oscilloscope 
#https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython
 
#step 3 :-  install the ADC packages from Adafruit by using pip3
#$ sudo pip3 install adafruit-circuitpython-ads1x15
#$ sudo pip3 install adafruit-blinka
 
#$ git clone https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
#$ cd Adafruit_CircuitPython_ADS1x15
#$ cd examples
 
#step 4 :- There will be a program name ads1x15_simpletest.py and run it by using python3
#$ python3 ads1x15_simpletest.py
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Optional: Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
