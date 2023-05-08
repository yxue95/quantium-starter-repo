import pandas as pd
import dash
from dash import dcc
from dash import html

# Read in the data from the CSV file
df = pd.read_csv('print_morsels.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Set the app layout
app.layout = html.Div(children=[
    # Header
    html.H1(children='Sales Data Visualizer'),

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
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
