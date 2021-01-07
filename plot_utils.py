#https://blog.heptanalytics.com/flask-plotly-dashboard/
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from config_utils.config import load_configs

def create_plot():
    
    configs = load_configs()
    csv_path = configs['sensor_data_path']
    sensor_data = pd.read_csv(csv_path)

    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        #go.Line(
        #    x=sensor_data['time'], # assign x as the dataframe column 'x'
        #    y=sensor_data['temperature_white']
        #),
        #go.Line(
        #    x=sensor_data['time'],
        #    y=sensor_data['temperature_green']
        #    title='Sensor Temperature'

        #)

        go.Line(
            
           x=sensor_data['time'],
           y=sensor_data['temperature_green'],
           
           

           )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
