from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

@app.route("/notifications")
def notifications():
    return jsonify({
        "service": "notification-service",
        "messages": [
            "Order placed",
            "Payment successful"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

