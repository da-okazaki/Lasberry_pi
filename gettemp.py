# coding: UTF-8
# RaspberryPiでDHT11センサーから温湿度データを取得

import time
import dht11
import RPi.GPIO as GPIO

#定義
#GPIO 14 as DHT11 data pin
Temp_sensor=14

#温湿度データ取得
def get_temp():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(pin=Temp_sensor)

    while True:
        #データ取得
        result = instance.read()
        return result.temperature,result.humidity

if __name__ == '__main__':
    try:
        while True:
            #温湿度データ取得
            temperature,humidity = get_temp()

            #画面出力
            if temperature == 0:
                continue
            print("Temperature = ",temperature,"C"," Humidity = ",humidity,"%")

            #指定された秒数スリープ
            time.sleep(5)

    except:
        pass