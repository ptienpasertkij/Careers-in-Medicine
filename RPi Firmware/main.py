import RPi.GPIO as GPIO
import time
from time import sleep
from gpiozero import Button
from gpiozero import LED
import atexit

button1 = Button(2)
button2 = Button(3)

# Input Switch definitions
switch1 = 2
switch2 = 3
switch3 = 4
switch4 = 17
switch5 = 27

# Relay definitions
led1_relay = 5
led2_relay = 6
led3_relay = 13
led4_relay = 19
led5_relay = 26
ledring_relay = 22

led1 = LED(led1_relay)
led2 = LED(led2_relay)
led3 = LED(led3_relay)
led4 = LED(led4_relay)
led5 = LED(led5_relay)
ledring = LED(ledring_relay)
all_led = [led1, led2, led3, led4, led5]

def turn_leds_off():
    for led in all_led:
        led.off()
    ledring.on()
    
def turn_leds_on():
    for led in all_led:
        led.off()
        led.on()
        sleep(0.2)
    ledring.off()

if __name__ == "__main__":
    turn_leds_off()
    sleep(0.5)
    while True:
        turn_leds_on()
        atexit.register(turn_leds_off)
    
    atexit.register(turn_leds_off)
