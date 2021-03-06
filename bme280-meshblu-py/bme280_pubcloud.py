#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from time import sleep
import json
import sys
#import bme280
from config import conf

def sensing():
    #return bme280.readData()
    dict = {"pressure":1008.85,"temperature":30.25,"humidity":"39.35"}
    return dict

def on_connect(client, userdata, rc):
    print("Connected with result code {}".format(rc))
    

def on_publish(client, userdata, mid):
    print("publish: {}".format(mid))

def main():
    # MQTT
    client = mqtt.Client(client_id='',
	                 clean_session=True, protocol=mqtt.MQTTv311)
    client.username_pw_set(conf["TRIGGER_1_UUID"], conf["TRIGGER_1_TOKEN"])
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(conf["IDCF_CHANNEL_URL"], 1883, 60)
    while True:
        sleep(5)
        retval = sensing()
        if retval:
             message = json.dumps({"devices": conf["ACTION_1_UUID"],
                                   "payload": retval})
             print(message)
             client.publish("message", message)
if __name__ == '__main__':
    main()
