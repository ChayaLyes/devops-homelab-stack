from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Homelab Stack 🚀",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "env": os.getenv("APP_ENV", "dev")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)