import flask
import dash
import random
import datetime
import dash_html_components as html
from flask import render_template
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from pyorbital.orbital import Orbital

server = flask.Flask(__name__)



#try :
#    satellite = Orbital("Aqua")
#except:
    # print('fail***************************************************************************************************************')
#    pass

#satellite = Orbital('TERRA')
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/', external_stylesheets=external_stylesheets
)
app.layout = html.Div( children=[
    html.Div([
        html.H4('GYM Xplane Flight Parameters  Live Feed'),
        html.Div( id='live-update-text',#style={'backgroundColor': 'red'}

        	),
        dcc.Graph(id='live-update-graph',#figure={'layout':{'height':900,'width':900}}

        	),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ]),
], #style={'backgroundColor': colors['background']} 

)

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    #lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    #style = {'padding': '5px', 'fontSize': '16px'}
    try:
        lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
       
    except :
        lon, lat, alt = random.randrange (60, 100, 20), random.randrange (1, 60, 20),  random.randrange (30, 80, 4)
        print('fail')
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Longitude: {0:.2f}'.format(lon), style=style),
        html.Span('Latitude: {0:.2f}'.format(lat), style=style),
        html.Span('Altitude: {0:0.2f}'.format(alt), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    #satellite = Orbital('TERRA')
    try:
        satellite = Orbital('TERRA')
    except:
        pass
    data = {
        'time': [],
        'Latitude': [],
        'Longitude': [],
        'Altitude': []
    }


    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        #lon, lat, alt = satellite.get_lonlatalt(
        #    time
        #)
        try:
            lon, lat, alt = satellite.get_lonlatalt(
            time
            )
        except:
            lon, lat, alt = random.randrange (1, 20, 1), random.randrange (-30, 20, 1),  random.randrange (30, 80, 4)
        data['Longitude'].append(lon)
        data['Latitude'].append(lat)
        data['Altitude'].append(alt)
        data['time'].append(time)

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=2, cols=2, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 10, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace ({
        'x': data['time'],
        'y': data['Altitude'],
        'name': 'Altitude',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)

    j = go.Scatter(
        x =data['Longitude'],
        y= data['Latitude'],
        text= data['time'],
        name= 'Longitude vs Latitude',
        mode= 'lines+markers',
        type= 'scatter'
    )

    fig.append_trace(j  , 2, 1)
    
    #fig.append_trace(j  , 2, 1)
    


    return fig


@server.route('/dash/map/')
def index():
    return render_template('globe.html')

#app.layout = html.Div("My Dash app")

if __name__ == '__main__':
    app.run_server(debug=True)