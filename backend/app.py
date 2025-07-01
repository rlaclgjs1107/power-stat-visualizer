from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})


if __name__ == "__main__":
    app.run()
