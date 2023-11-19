import re
from turtle import color
from flask import Flask, request
from flask_cors import CORS
from database.DatabaseConnect import DatabaseConnect
from module.functions import change_to_json

app = Flask(__name__)
CORS(app)

db = DatabaseConnect(); 

# output api
# poop
@app.route("/api/output/poop", methods = ["GET"])
def output_poop_get():
    data = db.conn_get("SELECT * FROM output_poop")
    data = change_to_json(data)
    return data;

@app.route("/api/output/poop", methods = ["POST"])
def output_poop_add():
    record_id = request.values['record_id']
    date = request.values['date']
    time = request.values['time']
    property_id = request.values['property_id']
    color_id = request.values['color_id']
    amount = request.values['amount']
    period = request.values['period']
    result = db.conn_other(f"INSERT INTO output_poop(record_id, date, time, property_id, color_id, amount, checked, period) VALUES ({record_id}, {date}, {time}, {property_id}, {color_id}, {amount}, false, {period})", "POST")
    return result;

@app.route("/api/output/poop", methods = ["DELETE"])
def output_poop_delete():
    output_poop_id = request.values['output_poop_id']
    record_id = request.values['record_id']
    result = db.conn_other(f"DELETE FROM output_poop WHERE output_poop_id = {output_poop_id} AND record_id = {record_id}", "DELETE")
    return result;

# pee
@app.route("/api/output/pee", methods = ["GET"])
def output_pee_get():
    data = db.conn_get("SELECT * FROM output_pee")
    data = change_to_json(data)
    return data;

@app.route("/api/output/pee", methods = ["POST"])
def output_pee_add():
    return;

@app.route("/api/output/pee", methods = ["DELETE"])
def output_pee_delete():
    return;

# vomit
@app.route("/api/output/vomit", methods = ["GET"])
def output_vomit_get():
    data = db.conn_get("SELECT * FROM output_vomit")
    data = change_to_json(data)
    return data;

@app.route("/api/output/vomit", methods = ["POST"])
def output_vomit_add():
    return;

@app.route("/api/output/vomit", methods = ["DELETE"])
def output_vomit_delete():
    return;

# input api
@app.route("/api/input", methods = ["GET"])
def input_get():
    data = db.conn_get("SELECT * FROM input")
    data = change_to_json(data)
    return data;

@app.route("/api/input", methods = ["POST"])
def input_add():
    return;

@app.route("/api/input", methods = ["DELETE"])
def input_delete():
    return;

if __name__ == '__main__':
    app.run()