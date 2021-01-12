#https://blog.heptanalytics.com/flask-plotly-dashboard/
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from config_utils.config import load_configs
import pydevd_pycharm
import os
#pydevd_pycharm.settrace('192.168.0.68', port=1025, stdoutToServer=True, stderrToServer=True)

def create_plot():
    
    configs = load_configs()
    data_dir = configs['data_dir']
    csvs = os.listdir(data_dir)

    csv_path = os.path.join(data_dir,csvs[0])
    sensor_data = pd.read_csv(csv_path)
    graphs = []
    for k in sensor_data.keys():
        if k != 'time':
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=sensor_data['time'],
                    y=sensor_data[k],
                    name=csvs[0],
                )
            )
            for i,f in enumerate(csvs):
                if i !=0:
                    csv_path = os.path.join(data_dir, f)
                    sensor_data = pd.read_csv(csv_path)
                    fig.add_trace(
                        go.Scatter(
                            x=sensor_data['time'],
                            y=sensor_data[k],
                            name=f
                        )
                    )



            fig.update_layout(title_text=k)
            data = fig
            graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
            graphs.append(graphJSON)



    return graphs
create_plot()