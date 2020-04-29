from flask import Flask, render_template
import datetime
from miplant import MiPlant

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tom')
def tom():
    return render_template('tom.html')

@app.route('/sensor')
def get_sensor_readings():
    sensor = MiPlant(address = 'c4:7c:8d:66:64:39')
    sensor.read()
    template_data = {'temperature': str(sensor.temperature),
            'battery_level':sensor.battery,
            'Light' : sensor.light,
            'moisture' : sensor.moisture,
            'conductivity' : sensor.conductivity}

    return render_template('sensor.html', **template_data)

@app.route('/time')
def get_time():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {'title' : 'get time and data', 'time' : time_string}
    return render_template('time.html', **template_data)

if __name__ =="__main__":    
    app.run(debug=True, host = '0.0.0.0')
