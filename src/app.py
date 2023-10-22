from flask import Flask

app = Flask(__name__)

@app.route("/api", methods = ["GET"])
def get():
    return;

@app.route("/api", methods = ["POST"])
def add():
    return;

@app.route("/api", methods = ["PUT"])
def update_part():
    return;

@app.route("/api", methods = ["PATCH"])
def update_all():
    return;

@app.route("/api", methods = ["DELETE"])
def delete():
    return;
