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
    graphs = []
    for k in sensor_data.keys():
        if k != 'time':
            fig = go.Figure()    
            fig.add_trace(
                go.Line(
                    x=sensor_data['time'],
                    y=sensor_data[k]      
                )
            )
            fig.update_layout(title_text=k)
            data = fig
            graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
            graphs.append(graphJSON)

    

    return graphs
