import RPi.GPIO as GPIO
import time

LED = 14
BUTTON = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = False

try:
    while True:
        if GPIO.input(BUTTON):
            state = not state
            GPIO.output(LED, state)
            time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()
