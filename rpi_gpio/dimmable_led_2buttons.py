import RPi.GPIO as GPIO
import time

LED = 14
BTN_UP = 18
BTN_DOWN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm = GPIO.PWM(LED, 100)
pwm.start(0)

duty = 0

try:
    while True:
        if GPIO.input(BTN_UP):
            duty += 10
            if duty > 100:
                duty = 100
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.3)

        if GPIO.input(BTN_DOWN):
            duty -= 10
            if duty < 0:
                duty = 0
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.3)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
