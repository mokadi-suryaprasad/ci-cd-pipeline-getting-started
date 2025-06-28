from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Python Demo App"

@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})

@app.route("/subtract")
def subtract():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a - b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
