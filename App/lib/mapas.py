###########################################################################
# importar librerias generales de dash
###########################################################################

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

#     locs = ['ANTIOQUIA', 'ATLANTICO', 'BOLIVAR', 'CUNDINAMARCA', 'SANTAFE DE BOGOTA D.C']
    locs =['ANTIOQUIA','ATLANTICO','QUINDIO','SANTANDER','MAGDALENA','META','CUNDINAMARCA',
           'TOLIMA','CALDAS','HUILA','CORDOBA','RISARALDA','BOYACA','NARIÑO','CAUCA',
           'NORTE DE SANTANDER','SANTAFE DE BOGOTA D.C','VALLE DEL CAUCA','BOLIVAR']
    
#     locs =['MEDELLIN','BARRANQUILLA','SANTA MARTA'.'ARMENIA','BUCARAMANGA','TUNJA','CALI','IBAGUE','CARTAGENA',
#            'VILLAVICENCIO','NEIVA','MANIZALES','PEREIRA','PASTO','CUCUTA','POPAYAN','SANTAFE DE BOGOTA D.C','MONTERIA']

#     for loc in countries['objects']['mpios']['geometries']:
#     loc['id'] = loc['properties']['name']
    
    for loc in countries['features']:
        loc['id'] = loc['properties']['NOMBRE_DPT']
    Map_Fig = go.Figure(go.Choroplethmapbox(
                        geojson=countries,
                        locations=locs,
                        z=[18,16,13,15,17,13,13,13,13,13,13,13,13,13,13,13,19,17,14],
                        colorscale='ylgnbu',
                        colorbar_title="Dpto"))
    Map_Fig.update_layout(mapbox_style="carto-positron",
                            mapbox_zoom=5,
                            height=800,
                            mapbox_center = {"lat": 4.570868, "lon": -74.2973328})

###########################################################################
# define el mapas
###########################################################################

mapa_01 = html.Div([
                    dcc.Graph(figure=Map_Fig, id='COL_map')
                ], id='id_mapa_col')