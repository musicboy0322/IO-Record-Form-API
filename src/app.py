from flask import Flask

app = Flask(__name__)

# output api
# poop
@app.route("/api/output/poop", methods = ["GET"])
def get():
    return;

@app.route("/api/output/poop", methods = ["POST"])
def add():
    return;

@app.route("/api/output/poop", methods = ["DELETE"])
def delete():
    return;

# pee
@app.route("/api/output/pee", methods = ["GET"])
def get():
    return;

@app.route("/api/output/pee", methods = ["POST"])
def add():
    return;

@app.route("/api/output/pee", methods = ["DELETE"])
def delete():
    return;

# vomit
@app.route("/api/output/vomit", methods = ["GET"])
def get():
    return;

@app.route("/api/output/vomit", methods = ["POST"])
def add():
    return;

@app.route("/api/output/vomit", methods = ["DELETE"])
def delete():
    return;

# input api
@app.route("/api/input", methods = ["GET"])
def get():
    return;

@app.route("/api/input", methods = ["POST"])
def add():
    return;

@app.route("/api/input", methods = ["DELETE"])
def delete():
    return;