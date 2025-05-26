#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import config

print("main kiln relay configured as config.gpio_main_kiln_relay = %s BCM pin\n" % (config.gpio_main_kiln_relay))

# Define the GPIO pin number
RELAY_PIN = config.gpio_main_kiln_relay
print("pin:")
print(RELAY_PIN)
# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn ON relay
        time.sleep(3)                      # Wait 3 seconds
        GPIO.output(RELAY_PIN, GPIO.LOW)   # Turn OFF relay
        time.sleep(3)                      # Wait 3 seconds

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    GPIO.cleanup()