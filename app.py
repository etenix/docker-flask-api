from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Log setting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Guest")

    app.logger.info(f"Request received: name={name}")

    return jsonify({
        "message": f"Hello {name}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)