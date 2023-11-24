from flask import Flask, request
from flask_cors import CORS
from database.DatabaseConnect import DatabaseConnect
from module.functions import change_to_json

app = Flask(__name__)
CORS(app)

db = DatabaseConnect(); 

# output api
# poop
@app.route("/api/output/poop/<date>/<record_id>", methods = ["GET"])
def output_poop_get(date, record_id):
    data = db.conn_get(f"SELECT output_poop_id, record_id, date, time, property, color, amount, checked, period FROM output_poop LEFT JOIN output_poop_property ON output_poop.property_id = output_poop_property.property_id LEFT JOIN output_poop_color ON output_poop.color_id = output_poop_color.color_id WHERE date = {date} AND record_id = {record_id};")
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
    result = db.conn_other(f"INSERT INTO output_poop(record_id, date, time, property_id, color_id, amount, checked, period) VALUES ({record_id}, {date}, {time}, {property_id}, {color_id}, {amount}, false, {period});", "POST")
    return result;

@app.route("/api/output/poop", methods = ["DELETE"])
def output_poop_delete():
    output_poop_id = request.values['output_poop_id']
    record_id = request.values['record_id']
    result = db.conn_other(f"DELETE FROM output_poop WHERE output_poop_id = {output_poop_id} AND record_id = {record_id};", "DELETE")
    return result;

# pee
@app.route("/api/output/pee/<date>/<record_id>", methods = ["GET"])
def output_pee_get(date, record_id):
    data = db.conn_get(f"SELECT output_pee_id, record_id, date, time, color, amount, checked, period FROM output_pee LEFT JOIN output_pee_color ON output_pee.color_id = output_pee_color.color_id WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/output/pee", methods = ["POST"])
def output_pee_add():
    record_id = request.values['record_id']
    date = request.values['date']
    time = request.values['time']
    color_id = request.values['color_id']
    amount = request.values['amount']
    period = request.values['period']
    result = db.conn_other(f"INSERT INTO output_pee(record_id, date, time, color_id, amount, checked, period) VALUES ({record_id}, {date}, {time}, {color_id}, {amount}, false, {period});", "POST")
    return result;

@app.route("/api/output/pee", methods = ["DELETE"])
def output_pee_delete():
    output_pee_id = request.values['output_pee_id']
    record_id = request.values['record_id']
    result = db.conn_other(f"DELETE FROM output_pee WHERE output_pee_id = {output_pee_id} AND record_id = {record_id};", "DELETE")
    return result;

# vomit
@app.route("/api/output/vomit/<date>/<record_id>", methods = ["GET"])
def output_vomit_get(date, record_id):
    data = db.conn_get(f"SELECT * FROM output_vomit WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/output/vomit", methods = ["POST"])
def output_vomit_add():
    record_id = request.values['record_id']
    date = request.values['date']
    time = request.values['time']
    amount = request.values['amount']
    period = request.values['period']
    result = db.conn_other(f"INSERT INTO output_vomit(record_id, date, time, amount, checked, period) VALUES ({record_id}, {date}, {time}, {amount}, false, {period});", "POST")
    return result;


@app.route("/api/output/vomit", methods = ["DELETE"])
def output_vomit_delete():
    output_vomit_id = request.values['output_vomit_id']
    record_id = request.values['record_id']
    result = db.conn_other(f"DELETE FROM output_vomit WHERE output_vomit_id = {output_vomit_id} AND record_id = {record_id};", "DELETE")
    return result;

# input api
@app.route("/api/input/<date>/<record_id>", methods = ["GET"])
def input_get(date, record_id):
    data = db.conn_get(f"SELECT * FROM input WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/input", methods = ["POST"])
def input_add():
    record_id = request.values['record_id']
    date = request.values['date']
    time = request.values['time']
    state = request.values['state']
    category = request.values['category']
    amount = request.values['amount']
    period = request.values['period']
    result = db.conn_other(f"INSERT INTO input(record_id, date, time, state, category, amount, checked, period) VALUES({record_id}, {date}, {time}, '{state}', '{category}', {amount}, false, {period});", "POST")
    return result;


@app.route("/api/input", methods = ["DELETE"])
def input_delete():
    input_id = request.values['input_id']
    record_id = request.values['record_id']
    result = db.conn_other(f"DELETE FROM input WHERE input_id = {input_id} AND record_id = {record_id};", "DELETE")
    return result;

# patient api
@app.route("/api/patient", methods = ["GET"])
def patient_get():
    data = db.conn_get(f"SELECT * FROM record;")
    data = change_to_json(data)
    return data;

@app.route("/api/patient/<record_id>", methods = ["GET"])
def patient_get_specific(record_id):
    data = db.conn_get(f"SELECT * FROM record WHERE record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/patient/register", methods = ["UPDATE"])
def patient_register():
    table = request.values['table']
    table_id = request.values['table_id']
    id = request.values['id']
    record_id = request.values['record_id']
    print(f"UPDATE {table} SET checked = true WHERE {table_id} = {id} AND record_id = {record_id};")
    result = db.conn_other(f"UPDATE {table} SET checked = true WHERE {table_id} = {id} AND record_id = {record_id};", "UPDATE")
    return result

if __name__ == '__main__':
    app.run()