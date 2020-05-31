import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import json
import urllib
import pandas as pd


def read_geojson():
    with open('geojsons/barrios.geojson', encoding="latin-1") as f:
        data = json.loads(f.read())
    return data


def get_fig():
    df = pd.read_csv('csvs/density_by_barrio.csv')
    geojson = read_geojson()

    fig = px.choropleth_mapbox(df, geojson=geojson, color="density",
                               locations="code", featureidkey="properties.codigo",
                               mapbox_style="carto-positron",
                               zoom=10, center={"lat": -34.8414, "lon": -56.1422},
                               opacity=0.5,
                               )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1('Probando choropleth'),
    dcc.Graph(figure=get_fig()),
])

# TODO conseguir un geojson mas chico o ver la forma de reducirle la definicion, al exportar el shp de departamentos queda un archivo de 9 MB
# TODO barrios.geojson lo consegui de https://github.com/vierja/geojson_montevideo/blob/master/barrios.geojson

if __name__ == '__main__':
    app.run_server()
