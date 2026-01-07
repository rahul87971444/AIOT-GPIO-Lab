from gpiozero import LED
from time import sleep

led = LED(14)

led.on()
sleep(5)
led.off()
