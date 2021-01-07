#!/usr/bin/env python3
from flask import Flask, render_template
import datetime
from miplant import MiPlant
from sensor_utils import MiSensor, device_2
from plot_utils import create_plot
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tom')
def tom():
    return render_template('tom.html')

@app.route('/plot')
def plot():
    graph = create_plot()
    return render_template('plot.html', plot=graph)

@app.route('/sensor')
def get_sensor_readings():
    sensor = MiSensor(device_2)

    template_data = {'temperature': str(sensor.get_temperature()),
            'battery_level':str(sensor.get_battery()),
            'light' : str(sensor.get_light()),
            'moisture' : str(sensor.get_moisture()),
            'conductivity' : str(sensor.get_conductivity())
            }

    return render_template('sensor.html', **template_data)

@app.route('/time')
def get_time():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {'title' : 'get time and data', 'time' : time_string}
    return render_template('time.html', **template_data)

if __name__ =="__main__":    
    app.run(debug=True, host = '0.0.0.0')
