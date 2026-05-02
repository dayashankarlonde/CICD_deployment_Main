from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend working successfully",
        "status": "ok"
    })

@app.route("/api/data")
def data():
    return jsonify([
        {"id": 1, "name": "Aman"},
        {"id": 2, "name": "Rahul"}
    ])

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)