###########################################################################
# importar librerias generales de dash
###########################################################################
import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
import dash_table as dte
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate


import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output, State, ClientsideFunction

###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################

import json
import certifi
import ssl
import requests
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime as dt
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text
from urllib.request import urlopen

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas, filtros

###########################################################################
# cargar mapas
###########################################################################

with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    countries = json.load(response)

# with open('../data/col.json') as geo:
#     countries = json.loads(geo.read())

###########################################################################
# crear mapas
###########################################################################

locs =['ANTIOQUIA','ATLANTICO','QUINDIO','SANTANDER','MAGDALENA','META','CUNDINAMARCA',
           'TOLIMA','CALDAS','HUILA','CORDOBA','RISARALDA','BOYACA','NARIÑO','CAUCA',
           'NORTE DE SANTANDER','SANTAFE DE BOGOTA D.C','VALLE DEL CAUCA','BOLIVAR']
df_mapas=consultas.df_mapa
                       
for loc in countries['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']
trace_1 = go.Choroplethmapbox(
                        geojson=countries,
                        locations=df_mapas['dpto'],
                        z=df_mapas['N_Efectivas'],
                        colorscale='ylgnbu',# zmin=0, zmax=12,
                        marker_opacity=0.5, marker_line_width=0)
layout = go.Layout(mapbox_style="carto-positron",height=700,width=550,
                  mapbox_zoom=5, mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                  margin={"r":0,"t":0,"l":0,"b":0})
fig = go.Figure(data = [trace_1], layout = layout)


###########################################################################
# define el mapas
###########################################################################

mapa_01 = html.Div([dcc.Graph(figure=fig, id='id_map')], id='id_mapa_col')
