import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC  = "sensors/raspi/dht11/telemetry"

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker, rc=", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode('utf-8', errors='ignore')}")

client = mqtt.Client(client_id="ec2-subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()