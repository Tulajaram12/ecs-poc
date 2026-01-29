from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

@app.route("/orders")
def orders():
    return jsonify({
        "service": "order-service",
        "orders": [
            {"id": 1, "item": "laptop"},
            {"id": 2, "item": "phone"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

