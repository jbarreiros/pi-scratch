import RPi.GPIO as GPIO
import time

def init(leds):
    GPIO.setmode(GPIO.BCM)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        off(led)

def on(*leds):
    for led in leds:
        GPIO.output(led, True)

def off(*leds):
    for led in leds:
        GPIO.output(led, False)

def cleanup():
    GPIO.cleanup()

def middle_out(leds, sleep):
    i = 3
    j = 4

    while True:
        on(leds[i], leds[j])

        if i < 3:
            off(leds[i+1], leds[j-1])

        time.sleep(sleep)

        if i == 0:
            off(leds[i], leds[j])
            time.sleep(sleep)
            i = 3
            j = 4
        else:
            i = i - 1
            j = j + 1

def back_and_forth(leds, sleep):
    i = 0
    max = (len(leds) - 1)

    while True:
        on(leds[i])

        if i == 0:
            off(leds[max])
        elif i > 0:
            off(leds[i-1])

        time.sleep(sleep)
        i = i + 1

        if i > max:
            leds.reverse()
            i = 0
