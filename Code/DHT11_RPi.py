import dht11
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

DHT11_PIN = 18

sensor = dht11.DHT11(pin=DHT11_PIN)
while True:
    result = sensor.read()
    print("temperature: ",result.temperature)
    print("humidity: ",result.humidity)
    time.sleep(2)




