from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "data.csv"

with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature", "humidity"])

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>IoT DHT Sensor Server</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }
                .container { background: white; padding: 30px; border-radius: 10px; max-width: 600px; margin: 0 auto; }
                h1 { color: #333; }
                code { background: #e0e0e0; padding: 2px 6px; border-radius: 3px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌡️ IoT DHT Sensor Server</h1>
                <p>Servidor activo y listo para recibir datos de temperatura y humedad.</p>
                <h2>Endpoints disponibles:</h2>
                <ul>
                    <li><code>POST /data</code> - Recibe datos de sensores</li>
                </ul>
                <h2>Formato de datos esperado:</h2>
                <pre>
{
    "temperature": 25.5,
    "humidity": 60.2
}
                </pre>
                <p>Los datos se guardan automáticamente en <code>data.csv</code></p>
            </div>
        </body>
    </html>
    """

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, temperature, humidity])

    print(f"📥 Data received: {temperature}°C, {humidity}%")

    return jsonify({"status": "ok", "message": "Data received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
