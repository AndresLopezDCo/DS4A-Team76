###########################################################################
# importar librerias generales de dash
###########################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate

###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################

import pathlib
import math
import numpy as np
import datetime as dt
import pandas as pd
import json
import plotly.graph_objects as go 
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas, filtros

###########################################################################
# creamos variables por graficas
###########################################################################

fig_ejemplo1 = px.scatter(consultas.df_ejemplo, x='edad', y='codenc', height=400)
fig_ejemplo2 = px.line(consultas.df_ejemplo, x='edad', y='codenc', height=400)
fig_ejemplo3 = px.scatter(consultas.df_ejemplo, x='edad', y='codenc', height=400)
fig_ejemplo4 = px.box(consultas.df_ejemplo, y="edad")

###########################################################################
# grafica distribucion por rango de edad barras
###########################################################################

grafica_01 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo1,id='id_figure_01')
                ],id='id_grafica_01')

###########################################################################
# grafica distribucion por rango de edad lineas
###########################################################################

grafica_02 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo2,id='id_figure_02')
                ],id='id_grafica_02')

###########################################################################
# grafica distribucion por rango de edad plots
###########################################################################

grafica_03 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo3,id='id_figure_03')
                ],id='id_grafica_03')

###########################################################################
# grafica distribucion por rango de edad boxplot
###########################################################################

grafica_04 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo4,id='id_figure_04')
                ],id='id_grafica_04')
