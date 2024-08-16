#!/usr/bin/python

# Mengawal kipas secara automatik untuk sistem penyejukkan CPU Raspberry PI 3 B+
# Sistem ini akan feed datanya kepada IoT Platfrom ThingSpeak, bila suhu sampai
# atau lebih 50c, ThingSpeak akan hantar tweet ke Twitter @Abe_key. Sila rujuk 
# file iot.py untuk details.
# Nak guna relay 1 channel 3.3V - 17 / Ogos / 2024 (12:00am)

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
GPIO.setup(16, GPIO.OUT) # Output data untuk kipas sambung ke relay 3.3V
GPIO.setup(20, GPIO.OUT) # Untuk ON LED Merah, nak royat kipas tengah musing
GPIO.setup(21, GPIO.OUT) # Untuk ON LED Hijau, nak royat kipas tak musing. Suhu CPU okay

#Nak ambik bacaan suhu CPU semasa
def measure_temp():
    raw = os.popen('vcgencmd measure_temp').readline()
    m = re.match("temp=(\d+\.?\d*)'C", raw)
    if not m:
        raise ValueError("Unexpected temperature string: " + raw)
    return float(m.group(1))


while True:     # Loop sokmo sokmo

    print 'Suhu CPU: {}'.format(temp)

#kipas mula musing pada suhu 48.5c dan LED Merah pun nyalo, LED Hijau mapuh

    if temp >= 48.5:
        print 'Buka kipas'
        GPIO.output(16, True)
        GPIO.output(20, True)
        GPIO.output(21, False)

#kipas mapuh tak musing, LED Merah pun mapuh jugok, tapi LED Hijau nyala
    else:
        print 'Tutup kipas'
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)

#tunggu pusingan seterusnya 10 saat
    time.sleep(10)
