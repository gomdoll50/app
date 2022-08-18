
import json, time
#from urllib import parse
from flask import Flask, json, jsonify, request, abort, make_response, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/login',methods = ['GET'])
def login():
    return render_template("login.html")

@app.route('/get', methods=['GET'])
def get():
    f = open('SENSOR.json',"r")
    rf_json = f.read()
    f.close()
    return jsonify(rf_json)


@app.route('/<sensor_name>', methods=['GET'])
def get_data(sensor_name):
    f = open('SENSOR.json',"r")
    rf_json = f.read()
    f.close()
    sensor = json.loads(rf_json)

    return jsonify(sensor[sensor_name])

@app.route('/<sensor_name>/<sensor_id>', methods=['PUT'])
def put_data_id(sensor_name,sensor_id):
    f = open('SENSOR.json',"r")
    rf_json = f.read()
    f.close()
    sensors = json.loads(rf_json)
    #task = [task for task in sensors[sensor_name] if task["id"] == sensor_id]
    '''
    for idx,task in enumerate(sensors[sensor_name]):
        if task["id"] == sensor_id:
            break
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task = request.json
    task["id"] = sensor_id
    sensors[sensor_name][idx] = task
    '''
    if sensor_name == 'qr':
        str(sensor_id)
    else:
        int(sensor_id)
    sensors[sensor_name] = sensor_id
    f = open('SENSOR.json',"w")
    f.write(json.dumps(sensors))
    f.close()
    #print(task)
    print(123)
    print("%s %s" %sensor_name,sensor_id)

    return jsonify(sensors[sensor_name])
'''
@app.route('/<sensor_name>/<int:sensor_id>', methods=['DELETE'])
def delete_data_id(sensor_name,sensor_id):
    f = open('SENSOR.json',"r")
    rf_json = f.read()
    f.close()
    sensors = json.loads(rf_json)
    for idx,task in enumerate(sensors[sensor_name]):
        if task["id"] == sensor_id:
            break
    if task["id"] != sensor_id:
        abort(400)
    del(sensors[sensor_name][idx])
    f = open('SENSOR.json',"w")
    f.write(json.dumps(sensors,indent=2))
    f.close()
    return {
        "delete" : "success"
    }, 202  
  #return jsonify('{}')
'''
@app.route('/<sensor_name>', methods=['POST'])
def post_data(sensor_name):
    f = open('SENSOR.json',"r")
    rf_json = f.read()
    f.close()
    sensors = json.loads(rf_json)
    '''
    cnt_sensor = len(sensors[sensor_name])
    if not request.json:
        abort(400)
    task = request.json
    task["id"] = cnt_sensor+1
    sensors[sensor_name].append(task)
    '''
    f = open('SENSOR.json',"w")
    f.write(json.dumps(sensors,indent=2))
    f.close()
    return jsonify(task)




#if __name__ == '__main__':
#    app.run(host='192.168.0.119',  port=8000)
