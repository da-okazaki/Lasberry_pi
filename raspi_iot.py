'''
rasberrypi iot_test
'''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import getopt
import logging
import json
import datetime
import sys

# Raspberry Pi
import wiringpi as pi

PIR_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(PIR_PIN, pi.INPUT)


# MQTT Publish
CLIENT_ID = "test_client_id"
TOPIC     = "my/test"
DEVICE_NO = "100"
GATEWAY_NO = "1001"
ENDPOINT = "a2cu1q4uiivotl-ats.iot.ap-northeast-1.amazonaws.com"
PORT = 8883

ROOT_CA = "/home/pi/cert/AmazonRootCA1.pem"
PRIVATE_KEY = "/home/pi/cert/a554a4cca1-private.pem.key"
CERTIFICATE = "/home/pi/cert/a554a4cca1-certificate.pem.crt"

# Configure Logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)

# Init AWS IoTMQTTClient
client = AWSIoTMQTTClient(CLIENT_ID)
client.configureEndpoint(ENDPOINT, PORT)
client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)

# AWSIoTMQTTClient connection configuration
client.configureAutoReconnectBackoffTime(1, 32, 20)
client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

# Connect and subscribe to AWS IoT
client.connect()

try:


    while True:
        if (pi.digitalRead(PIR_PIN) == pi.HIGH):
            message = {}
            message['id'] = DEVICE_NO
            message['id2'] = GATEWAY_NO
            message['message'] = "detected"
            messageJson = json.dumps(message)
            print (messageJson)
            client.publish(TOPIC, messageJson, 1)
            time.sleep(5)
        else:
            message = {}
            message['id'] = DEVICE_NO
            message['id2'] = GATEWAY_NO
            message['message'] = "Not detected"
            messageJson = json.dumps(message)
            print (messageJson)
            client.publish(TOPIC, messageJson, 1)
            time.sleep(5)

except:
    import traceback
    traceback.print_exc()

print ("Terminated")
