import time, json, random
import paho.mqtt.client as mqtt

BROKER = "ubuntu@ec2-18-214-48-188.compute-1.amazonaws.com"
PORT = 1883
TOPIC  = "sensors/raspi/dht11/telemetry"

client = mqtt.Client(client_id="raspi-publisher")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        msg = {
            "temperature": round(24 + random.random()*6, 2),
            "humidity": round(45 + random.random()*20, 2)
        }
        client.publish(TOPIC, json.dumps(msg))
        print("Publicado:", msg)
        time.sleep(10)
except KeyboardInterrupt:
    print("Interrumpido por el usuario")
    pass
except Exception as e:
    print("Error sending data:", e)
finally:
    client.loop_stop()
    client.disconnect()