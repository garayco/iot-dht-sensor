import time
import board
import adafruit_dht
import requests

dhtDevice = adafruit_dht.DHT11(board.D4)
AWS_SERVER = "ec2-3-80-100-169.compute-1.amazonaws.com:5000"
SERVER_URL = f"http://{AWS_SERVER}/data"

while True:
    try:
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity
        data = {"temperatura": temp, "humedad": hum}
        print(f"Enviando: {data}")
        requests.post(SERVER_URL, json=data)
    except Exception as e:
        print("Error:", e)
    time.sleep(10)
