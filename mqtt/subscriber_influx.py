import json
from datetime import datetime, timezone
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(Path(__file__).with_name(".env"))
INFLUX_INIT_ADMIN_TOKEN = os.environ["INFLUX_INIT_ADMIN_TOKEN"]
INFLUX_INIT_ORG = os.environ["INFLUX_INIT_ORG"]
INFLUX_INIT_BUCKET = os.environ["INFLUX_INIT_BUCKET"]

# MQTT
BROKER = "localhost"
PORT   = 1883
TOPIC  = "sensors/raspi/dht11/telemetry"

# InfluxDB
INFLUX_URL   = "http://localhost:8086"
INFLUX_TOKEN = INFLUX_INIT_ADMIN_TOKEN
ORG          = INFLUX_INIT_ORG
BUCKET       = INFLUX_INIT_BUCKET

client_influx = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=ORG)
write_api = client_influx.write_api()

def on_connect(client, userdata, flags, rc, properties=None):
    print("MQTT conectado (rc=", rc, ")")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        temp = float(data.get("temperature"))
        hum  = float(data.get("humidity"))
    except Exception:
        print("Payload no válido:", msg.payload)
        return

    p = (
        Point("env")
        .tag("device", "raspi")
        .tag("sensor", "dht11")
        .field("temperature", temp)
        .field("humidity", hum)
        .time(datetime.now(timezone.utc), WritePrecision.S)
    )
    write_api.write(bucket=BUCKET, record=p)
    print(f"OK -> [{msg.topic}] - Influx: temp={temp}, hum={hum}")

def main():
    client = mqtt.Client(client_id="ec2-influx-subscriber")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()