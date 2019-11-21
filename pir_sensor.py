# coding: utf-8
import wiringpi as pi
import time

PIR_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(PIR_PIN, pi.INPUT)

while True:
    if (pi.digitalRead(PIR_PIN) == pi.HIGH):
        #print("A person was detected.")
        print("detected")
        time.sleep(3)
    else:
        print("Not detected")
        time.sleep(3)
