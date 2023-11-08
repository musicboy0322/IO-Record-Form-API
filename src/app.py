from flask import Flask

app = Flask(__name__)

# output api
# poop
@app.route("/api/output/poop", methods = ["GET"])
def output_poop_get():
    return "asdasdasdsa";

@app.route("/api/output/poop", methods = ["POST"])
def output_poop_add():
    return;

@app.route("/api/output/poop", methods = ["DELETE"])
def output_poop_delete():
    return;

# pee
@app.route("/api/output/pee", methods = ["GET"])
def output_pee_get():
    return;

@app.route("/api/output/pee", methods = ["POST"])
def output_pee_add():
    return;

@app.route("/api/output/pee", methods = ["DELETE"])
def output_pee_delete():
    return;

# vomit
@app.route("/api/output/vomit", methods = ["GET"])
def output_vomit_get():
    return;

@app.route("/api/output/vomit", methods = ["POST"])
def output_vomit_add():
    return;

@app.route("/api/output/vomit", methods = ["DELETE"])
def output_vomit_delete():
    return;

# input api
@app.route("/api/input", methods = ["GET"])
def input_get():
    return;

@app.route("/api/input", methods = ["POST"])
def input_add():
    return;

@app.route("/api/input", methods = ["DELETE"])
def input_delete():
    return;

if __name__ == '__main__':
    app.run()