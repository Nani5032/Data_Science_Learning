import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output

# external css style sheets

external_stylesheets = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
        "crossorigin": "anonymous",
    }
]

patients = pd.read_csv('IndividualDetails.csv')
total_cases = patients.shape[0]
active_cases = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deaths = patients[patients['current_status'] == 'Deceased'].shape[0]

options=[
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#app.layout=html.H1("Hello World")

app.layout = html.Div([
    html.H1("Corona virus pandemic", style={'color':'#fff', 'text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total cases", className='text-light'),
                    html.H4(total_cases, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active cases", className='text-light'),
                    html.H4(active_cases, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3')
    ], className='row'),
    html.Div([], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row')
], className='container')

@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):
    if type=='All':
        patient_bar = patients['detected_state'].value_counts().reset_index()
        return {'data': [go.Bar(x=patient_bar['index'], y=patient_bar['detected_state'])],
                'layout': go.Layout(title='state total count')}
    else:
        no_of_patients = patients[patients['current_status'] == type]
        patient_bar = no_of_patients['detected_state'].value_counts().reset_index()
        return {'data': [go.Bar(x=patient_bar['index'], y=patient_bar['detected_state'])],
                'layout': go.Layout(title='state total count')}

if __name__ == "__main__":
    app.run_server(debug=True)