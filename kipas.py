#!/usr/bin/python

# Mengawal kipas secara automatik untuk sistem penyejukkan CPU Raspberry PI 3 B+
# Sistem ini akan feed datanya kepada IoT Platfrom ThingSpeak, bila suhu sampai
# atau lebih 50c, ThingSpeak akan hantar tweet ke Twitter @Abe_key. Sila rujuk 
# file iot.py untuk details.

# Ditulis pada 14 Mei, 2020 bersama Abe Din (9M2CIO)
# de 9W2KEY OJ15dx
# 73

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import re
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) # Output data untuk kipas sambung ke kaki tengah NPN transistor
GPIO.setup(26, GPIO.OUT) # Untuk ON LED, nak royat kipas tengah musing

#Nak ambik bacaan suhu CPU semasa
def measure_temp():
    raw = os.popen('vcgencmd measure_temp').readline()
    m = re.match("temp=(\d+\.?\d*)'C", raw)
    if not m:
        raise ValueError("Unexpected temperature string: " + raw)
    return float(m.group(1))


while True:     # Loop sokmo sokmo

    print 'Suhu CPU: {}'.format(temp)

#kipas mula musing pada suhu 48.5c dan LED pun nyalo

    if temp >= 48.5:
        print 'Buka kipas'
        GPIO.output(14, True)
        GPIO.output(26, True)

#kipas mapuh tak musing, LED pun mapuh jugok
    else:
        print 'Tutup kipas'
        GPIO.output(14, False)
        GPIO.output(26, False)

#tunggu pusingan seterusnya 10 saat
    time.sleep(10)
