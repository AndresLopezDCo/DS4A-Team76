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
# creamos filtro de mapa
###########################################################################

filtro_01 = html.Div (children=[
                    html.Label('FILTRO MAPA', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'LLAMADAS EFECTIVAS', 'value': '1'}
                            ,{'label': 'DURACION LLAMADAS', 'value': '2'}
                            ,{'label': 'NUMERO DE CUOTAS', 'value': '3'}
                            ,{'label': 'PORC LLAMADAS EFECTIVAS', 'value': '4'}
                        ],id='id_flt_mapa_01',value='1')
                ],id='id_filtro_01',className='filtros')

###########################################################################
# creamos filtro de grafica
###########################################################################

filtro_1001 = html.Div (children=[
                    html.Label('TIPO_GRAFICO', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'BARRAS', 'value': '1'}
                            ,{'label': 'LINEAS', 'value': '2'}
                            ,{'label': 'SCATERPLOT', 'value': '3'}
                            ,{'label': 'BOXPLOT', 'value': '4'}
                        ],id='tipo_grafico_01',value='1')
                ],id='filtro_1001',className='filtros')

###########################################################################
# creamos filtro de slider de prueba por estrato
###########################################################################

filtro_02 = html.Div (children=[
                    html.Label('ESTRATO VRS 2', className='filtros-label')
                    ,dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=6,
                        step=1,
                        value=3,
                        #mark={1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6'},
                    ), html.Div(id='id_filtro_02')
                ],id='filtro_02',className='filtros')

