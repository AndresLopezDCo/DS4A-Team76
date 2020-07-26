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


df1 = consultas.df_ejemplo_01
ejex1 = 'edad'
ejey1 = 'codenc'

df2 = consultas.df_ejemplo_02
ejex2 = 'estrato'
ejey2 = 'codenc'


fig_ejemplo1 = px.bar(df1, x=ejex1, y=ejey1, height=400)
fig_ejemplo2 = px.line(df1, x=ejex1, y=ejey1, height=400)
fig_ejemplo3 = px.scatter(df1, x=ejex1, y=ejey1, height=400)
fig_ejemplo4 = px.box(df1, x=ejex1, y=ejey1)

fig_ejemplo5 = px.bar(df2, x=ejex2, y=ejey2, height=400)
fig_ejemplo6 = px.scatter(df2, x=ejex2, y=ejey2, height=400)

###########################################################################
# grafica distribucion por rango de edad
###########################################################################

grafica_01 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo1,id='id_figure_01')
                ],id='id_grafica_01')

###########################################################################
# grafica distribucion por estrato barras
###########################################################################

grafica_02 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo5,id='id_figure_02')
                ],id='id_grafica_02')

###########################################################################
# grafica distribucion por estrato scatter
###########################################################################

grafica_03 = html.Div ([
                    dcc.Graph(figure=fig_ejemplo6,id='id_figure_03')
                ],id='id_grafica_03')
