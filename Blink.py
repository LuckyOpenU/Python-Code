import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)

while True:
    GPIO.output(25, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(25, GPIO.LOW)
    time.sleep(.5)
