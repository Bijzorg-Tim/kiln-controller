#!/usr/bin/env python

import paho.mqtt.publish as publish
import config


MQTT_BROKER = config.MQTT_BROKER
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "kiln/status"
MQTT_MESSAGE = "started-profile"

# Optional username/password
MQTT_USERNAME = config.MQTT_USERNAME
MQTT_PASSWORD = config.MQTT_PASSWORD

publish.single(
    MQTT_TOPIC,
    payload=MQTT_MESSAGE,
    hostname=MQTT_BROKER,
    port=MQTT_PORT,
    auth={
        'username': MQTT_USERNAME,
        'password': MQTT_PASSWORD
    }
)