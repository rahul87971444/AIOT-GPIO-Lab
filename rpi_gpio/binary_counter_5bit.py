import RPi.GPIO as GPIO
import time

pins = [29, 31, 33, 35, 37]

GPIO.setmode(GPIO.BOARD)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    for count in range(32):
        binary = format(count, '05b')
        for i in range(5):
            GPIO.output(pins[i], int(binary[i]))
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
