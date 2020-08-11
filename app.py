
from flask import Flask, jsonify, render_template, request
import webbrowser
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request, jsonify
from firebase import firebase
import time

app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://temperaturemanagement-iot.firebaseio.com')

@app.route('/_room1', methods = ['GET'])
def room1():
    result1 = firebase.get('CurrentTempRoom1', 'Value')
    return jsonify(result=result1)


@app.route('/_room2', methods = ['GET'])
def room2():
    result = firebase.get('CurrentTempRoom2', 'Value')
    return jsonify(result2=result)

@app.route('/', methods=['POST','GET'])
def setRoom1():
    result = firebase.get('CurrentTempRoom1', 'Value')
    result2 = firebase.get('CurrentTempRoom2', 'Value')
    if request.method == 'POST':
        variable = request.form['content']
        firebase.put('DesiredTempRoom1', 'Value', int(variable))
        return render_template('index.html', data1 = result, data2 = result2)
    else:
        return render_template('index.html', data1 = result, data2 = result2)

@app.route('/setRoom2', methods=['POST','GET'])
def setRoom2():
    result = firebase.get('CurrentTempRoom1', 'Value')
    result2 = firebase.get('CurrentTempRoom2', 'Value')
    if request.method == 'POST':
        variable = request.form['content2']
        firebase.put('DesiredTempRoom2', 'Value', int(variable))
        return render_template('index.html', data1 = result, data2 = result2)
    else:
        return render_template('index.html', data1 = result, data2 = result2)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
