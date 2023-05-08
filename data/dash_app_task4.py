import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Read in the data from the CSV file
df = pd.read_csv('print_morsels.csv')

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'
])

# Define the radio button options
region_options = [{'label': 'North', 'value': 'north'},
                  {'label': 'East', 'value': 'east'},
                  {'label': 'South', 'value': 'south'},
                  {'label': 'West', 'value': 'west'},
                  {'label': 'All Regions', 'value': 'all'}]

# Set the app layout
app.layout = html.Div(children=[
    # Header
    html.H1(children='Sales Data Visualizer', className='text-center'),

    # Radio button for region filter
    dcc.RadioItems(
        id='region-filter',
        options=region_options,
        value='all',
        labelStyle={'display': 'inline-block', 'margin': '0 10px'},
        className='radio-items'
    ),

    # Line chart
    dcc.Graph(
        id='sales-chart',
        figure={
            'data': [
                {'x': df['date'], 'y': df['sales'], 'type': 'line', 'name': 'Sales'},
            ],
            'layout': {
                'title': 'Total Sales by Date',
                'xaxis': {'title': 'date'},
                'yaxis': {'title': 'sales'}
            }
        },
        className='graph-container'
    )
])

# Define the callback for updating the line chart based on the region filter
@app.callback(Output('sales-chart', 'figure'),
              Input('region-filter', 'value'))
def update_chart(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]

    return {
        'data': [
            {'x': filtered_df['date'], 'y': filtered_df['sales'], 'type': 'line', 'name': 'Sales'},
        ],
        'layout': {
            'title': 'Total Sales by Date ({})'.format(region),
            'xaxis': {'title': 'date'},
            'yaxis': {'title': 'sales'}
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)
