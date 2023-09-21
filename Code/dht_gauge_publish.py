import dht11
import RPi.GPIO as GPIO
import time 
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
temp_top = "kt/Paranthama A K/gauge/TEMP"
hum_top = "kt/Paranthama A K/gauge/HUM"

DHT11_PIN = 17

GPIO.setmode(GPIO.BCM) 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else: 
        print("Failed to connect",rc)
sensor = dht11.DHT11(pin=DHT11_PIN)
client=mqtt.Client()
client.on_connect = on_connect 
client.connect(broker, 1883)
while True:
    result = sensor.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity 
        print(int(temperature))
        print(int(humidity))
        client.publish(temp_top, int(temperature))
        client.publish(hum_top,int(humidity))
       # print(f"Temperature: {temperature} C, Humidity: {humidity}%")

    time.sleep(2)
client.loop_forever()
