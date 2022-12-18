# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from datetime import timedelta,date,datetime
import requests
import subprocess

app = Dash(__name__)

@app.callback(
    Output('textarea', 'value'),
    Input('input_url', 'value'))
def useApi(input_url):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    params = {
        'image_link': input_url,
    }
    response = requests.post('http://localhost:8000/net/image/prediction', params=params, headers=headers)
    return response.text


app.layout = html.Div(children=[
    html.H1(children='Food Image Prediction on url'),
    html.Div(style={'width': '32%', 'display': 'inline-block'}),
    html.Div(children=[
        html.Br(),
    ], style={'width': '32%', 'padding': 10, 'flex': 1, 'display': 'inline-block'}),
    html.Div(style={'width': '32%', 'display': 'inline-block'}),
    html.Div(children=[dcc.Input(
            id="input_url",
            type="url",
            value='',
            placeholder="input type url"
        )],style={'width': '32%', 'padding': 10, 'flex': 1, 'display': 'inline-block'}),
    html.Div(children=[
        dcc.Textarea(
        id='textarea',
        value='',
        style={'width': '100%', 'height': 150},
        )
        ], style={'width': '49%', 'display': 'inline-block'})

])




def start():    
    app.run_server(host='0.0.0.0', debug=False)
    subprocess.Popen(["uvicorn", "FastAPI:app", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == '__main__':
    start()