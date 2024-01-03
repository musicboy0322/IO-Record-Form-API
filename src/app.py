from flask import Flask, request
from flask_cors import CORS
from database.DatabaseConnect import DatabaseConnect
from database.RedisConnect import RedisConnect
from module.functions import change_to_json, split_amount_result, split_total_amount, split_vertification_result

app = Flask(__name__)
CORS(app)

db = DatabaseConnect()
redis = RedisConnect()

# output api
# poop
@app.route("/api/output/poop/<date>/<record_id>", methods = ["GET"])
def output_poop_get_patient(date, record_id):
    data = db.conn_get(f"SELECT output_poop_id, record_id, date, time, property, color, amount, checked, period FROM output_poop LEFT JOIN output_poop_property ON output_poop.property_id = output_poop_property.property_id LEFT JOIN output_poop_color ON output_poop.color_id = output_poop_color.color_id WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/output/poop/<date>/<record_id>/<period>", methods = ["GET"])
def output_poop_get_nurse(date, record_id, period):
    data = db.conn_get(f"SELECT output_poop_id, record_id, date, time, property, color, amount, checked, period FROM output_poop LEFT JOIN output_poop_property ON output_poop.property_id = output_poop_property.property_id LEFT JOIN output_poop_color ON output_poop.color_id = output_poop_color.color_id WHERE date = {date} AND record_id = {record_id} AND period = {period};")
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
def output_pee_get_patient(date, record_id):
    data = db.conn_get(f"SELECT output_pee_id, record_id, date, time, color, amount, checked, period FROM output_pee LEFT JOIN output_pee_color ON output_pee.color_id = output_pee_color.color_id WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/output/pee/<date>/<record_id>/<period>", methods = ["GET"])
def output_pee_get_nurse(date, record_id, period):
    data = db.conn_get(f"SELECT output_pee_id, record_id, date, time, color, amount, checked, period FROM output_pee LEFT JOIN output_pee_color ON output_pee.color_id = output_pee_color.color_id WHERE date = {date} AND record_id = {record_id} AND period = {period};")
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
def output_vomit_get_nurse(date, record_id):
    data = db.conn_get(f"SELECT * FROM output_vomit WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/output/vomit/<date>/<record_id>/<period>", methods = ["GET"])
def output_vomit_get_patient(date, record_id, period):
    data = db.conn_get(f"SELECT * FROM output_vomit WHERE date = {date} AND record_id = {record_id} AND period = {period};")
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
def input_get_patient(date, record_id):
    data = db.conn_get(f"SELECT * FROM input WHERE date = {date} AND record_id = {record_id};")
    data = change_to_json(data)
    return data;

@app.route("/api/input/<date>/<record_id>/<period>", methods = ["GET"])
def input_get_nurse(date, record_id, period):
    data = db.conn_get(f"SELECT * FROM input WHERE date = {date} AND record_id = {record_id} AND period = {period};")
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

@app.route("/api/patient/register", methods = ["PATCH"])
def patient_register():
    table = request.values['table']
    table_id = request.values['table_id']
    id = request.values['id']
    record_id = request.values['record_id']
    result = db.conn_other(f"UPDATE {table} SET checked = true WHERE {table_id} = {id} AND record_id = {record_id};", "UPDATE")
    return result

# nurse api
@app.route("/api/nurse/<account>/<password>", methods = ["GET"])
def nurse_get(account, password):
    try:
        data = db.conn_get(f"SELECT employee_id, name FROM password WHERE account = {account} AND password = {password}")
        data = change_to_json(data)
        if(len(data) == 2):
            return "Account not found"
        else:
            return data
    except Exception as e:
        return e

# amount api
@app.route("/api/input/amount/<date>/<record_id>/<period>/<state>", methods = ["GET"])
def amount_input_get(date, record_id, period, state):
    amount_count = db.conn_get(f"SELECT COUNT(*) FROM input WHERE date = {date} AND record_id = {record_id} AND period = {period} AND state = '{state}'")
    amount_count = split_amount_result(str(amount_count))
    key = date + record_id + period + state
    if(redis.conn().lindex(key, 0) == None):
        total_amount = db.conn_get(f"SELECT SUM(amount) FROM input WHERE date = {date} AND record_id = {record_id} AND period = {period} AND state = '{state}'")
        total_amount = split_total_amount(str(total_amount))
        redis.conn().lpush(key, amount_count, total_amount)
        redis.conn().expire(key, 86400)
        return str(total_amount)
    elif(redis.conn().lindex(key, 0) != amount_count):
        total_amount = db.conn_get(f"SELECT SUM(amount) FROM input WHERE date = {date} AND record_id = {record_id} AND period = {period} AND state = '{state}'")
        total_amount = split_total_amount(str(total_amount))
        redis.conn().lset(key, 0, amount_count)
        redis.conn().lset(key, 1, total_amount)
        redis.conn().expire(key, 86400)
        return str(total_amount)
    else: 
        total_amount = redis.conn().lindex(key, 1)
        return str(total_amount)

@app.route("/api/output/amount/<date>/<record_id>/<period>/<table>", methods = ["GET"])
def amount_output_get(date, record_id, period, table):
    amount_count = db.conn_get(f"SELECT COUNT(*) FROM {table} WHERE date = {date} AND record_id = {record_id} AND period = {period}")
    amount_count = split_amount_result(str(amount_count))
    key = date + record_id + period + table
    if(redis.conn().lindex(key, 0) == None):
        total_amount = db.conn_get(f"SELECT SUM(amount) FROM {table} WHERE date = {date} AND record_id = {record_id} AND period = {period}")
        total_amount = split_total_amount(str(total_amount))
        redis.conn().lpush(key, amount_count, total_amount)
        redis.conn().expire(key, 86400)
        return str(total_amount)
    elif(redis.conn().lindex(key, 0) != amount_count):
        total_amount = db.conn_get(f"SELECT SUM(amount) FROM {table} WHERE date = {date} AND record_id = {record_id} AND period = {period}")
        total_amount = split_total_amount(str(total_amount))
        redis.conn().lset(key, 0, amount_count)
        redis.conn().lset(key, 1, total_amount)
        redis.conn().expire(key, 86400)
        return str(total_amount)
    else: 
        total_amount = redis.conn().lindex(key, 1)
        return str(total_amount)

# vertification api
@app.route("/api/vertification/<record_id>/<vertification>", methods = ["GET"])
def vertification_get(record_id, vertification):
    result = db.conn_get(f"SELECT EXISTS(SELECT * FROM vertification WHERE record_id = '{record_id}' AND vertification = '{vertification}')")
    result = split_vertification_result(str(result))
    if(result == 1):
        return "Correct"
    else:
        return "Wrong"

if __name__ == '__main__':
    app.run()