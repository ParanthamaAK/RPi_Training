import dht11
import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the data pin of the DHT11 sensor
DHT11_PIN = 18

# Initialize the DHT11 sensor
sensor = dht11.DHT11(pin=DHT11_PIN)
while True:
    result = sensor.read()
    print("temperature: ",result.temperature)
    print("humidity: ",result.humidity)
    time.sleep(2)




