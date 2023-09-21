import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
temp_top = "kt/Paranthama A K/gauge/TEMP"
hum_top = "kt/Paranthama A K/gauge/HUM"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to MQTT Broker")
        client.subscribe(temp_top)
        client.subscribe(hum_top)
    else:
        print("Failed to connect",rc)

def on_message(client, userdata, msg):
    topic = msg.topic
    message = msg.payload.decode("utf-8")

    if topic == temp_top:
        print(f"Temperature: {message} C")
    elif topic == hum_top:
        print(f"Humidity: {message}%")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883)
client.loop_forever()
