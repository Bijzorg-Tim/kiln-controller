# #!/usr/bin/env python
# import config
# import adafruit_max31855
# import digitalio
# import time
# import datetime

# try:
#     import board
# except NotImplementedError:
#     print("not running a recognized blinka board, exiting...")
#     import sys
#     sys.exit()

# ########################################################################
# #
# # To test your gpio output to control a relay...
# #
# # Edit config.py and set the following in that file to match your
# # hardware setup: gpio_heat, gpio_heat_invert
# #
# # then run this script...
# # 
# # ./test-output.py
# #
# # This will switch the output on for five seconds and then off for five 
# # seconds. Measure the voltage between the output and any ground pin.
# # You can also run ./gpioreadall.py in another window to see the voltage
# # on your configured pin change.
# ########################################################################

# heater = digitalio.DigitalInOut(config.gpio_main_kiln_relay)
# heater.direction = digitalio.Direction.OUTPUT
# off = config.gpio_heat_invert
# on = not off

# print("\nboard: %s" % (board.board_id))
# print("heater configured as config.gpio_main_kiln_relay = %s BCM pin\n" % (config.gpio_main_kiln_relay))
# print("heater output pin configured as invert = %r\n" % (config.gpio_heat_invert))

import RPi.GPIO as GPIO
import time
import config


print("relay output pin configured as invert = %r\n" % (config.gpio_main_kiln_relay))

# Define the GPIO pin number
RELAY_PIN = config.gpio_main_kiln_relay
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