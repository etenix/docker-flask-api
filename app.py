from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Log setting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)

APP_NAME = os.getenv("APP_NAME", "Flask API")

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Guest")

    app.logger.info(f"[{APP_NAME}] Request: name={name}")

    return jsonify({
        "app": APP_NAME,
        "message": f"Hello {name}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)