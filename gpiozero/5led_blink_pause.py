from gpiozero import LED
from time import sleep

led = LED(14)

led.blink(on_time=1, off_time=1)
sleep(10)
led.off()
