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
import warnings
warnings.filterwarnings('ignore')

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas

###########################################################################
# creamos filtros
###########################################################################

filtro_01 = html.Div (children=[
                    html.Label('ESTRATO', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Estrato 1', 'value': '1'}
                            ,{'label': 'Estrato 2', 'value': '2'}
                            ,{'label': 'Estrato 3', 'value': '3'}
                            ,{'label': 'Estrato 4', 'value': '4'}
                            ,{'label': 'Estrato 5', 'value': '5'}
                            ,{'label': 'Estrato 6', 'value': '6'}
                        ],id='id_filtro_01',value=['1'] ,multi=True)
                ],id='filtro_01',className='filtros')

filtro_02 = html.Div (children=[
                    html.Label('ESTRATO VRS 2', className='filtros-label')
                    ,dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=6,
                        step=1,
                        value=3,
                    ), html.Div(id='id_filtro_02')
                ],id='filtro_02',className='filtros')
