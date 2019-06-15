# coding:utf-8
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import slackweb

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4) #←配線したGPIOピンの番号を指定

#取得した情報をslackwebに通知する
result = instance.read()
temp = result.temperature
humidity = result.humidity
nowtime = "{0:%Y/%m/%d %H:%M:%S}".format(datetime.datetime.now())
if humidity is not None and temp is not None:
    msg = u"{0} に測定した室内環境\n温度 : {1:0.1f}度\n湿度 : {2:0.1f}%\nCO2  : 997ppm\n気圧 : 1021.3hPa\n騒音 : 50dB\n\n快適な環境です。そのまま維持してください ٩(ˊᗜˋ*)و".format(nowtime,temp, humidity)
else:
    msg = u"温湿度を測定できませんでした"

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text=msg)
print msg