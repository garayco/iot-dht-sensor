import time
import requests
import random

AWS_SERVER = "ec2-3-90-2-201.compute-1.amazonaws.com:5000"
SERVER_URL = f"http://{AWS_SERVER}/data"
# SERVER_URL = f"https://{os.getenv('REPLIT_DEV_DOMAIN', 'localhost:5000')}/data"

while True:
    temp = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)

    data = {"temperature": temp, "humidity": humidity}
    print(f"Sending: {data}")
    

    try:
        response = requests.post(SERVER_URL, json=data)
        print(f"✅ Server response {response.status_code}: {response.json()}")
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(10)
