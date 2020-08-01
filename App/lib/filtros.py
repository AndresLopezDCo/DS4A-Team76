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
                    html.Label('VARIABLE', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Estrato', 'value': 'Estrato'}
                            ,{'label': 'Genero', 'value': 'Genero'}
                            ,{'label': 'Edad', 'value': 'etiquetas_rango_edad'}
                        ],id='id_efectivas_cuotas',value='Estrato')
                ],id='filtro_02',className='filtros')

###########################################################################
# creamos filtro de slider de prueba por estrato
###########################################################################

filtro_03 = html.Div (children=[
                    html.Label('TIEMPOS MARCADOR', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Llamadas', 'value':'calls'},
                            {'label': 'Duración total', 'value': 'total'},
                            {'label': 'Duración espera', 'value': 'espera'},
                            {'label': 'Duración hablado', 'value': 'hablado'},
                            {'label': 'Duración disponible', 'value': 'disponible'},
                            {'label': 'Duración pausas', 'value': 'pausas'},
                            {'label': 'Duración muerto', 'value': 'muerto'},
                            {'label': 'Duración efectivas', 'value': 'duracion_efectivas'}
                        ],id='id_marcador',value='calls')
                ],id='filtro_03',className='filtros')

###########################################################################
# creamos filtro de slider para modificar por mes los markdown
###########################################################################

filtro_04 = html.Div (children=[
                    html.Label('DURACIÓN [MESES]', className='filtros-label')
                    ,dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=26,
                        step=1,
                        value=6,
                        #mark={1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6'},
                    ), html.Div(id='id_filtro_04')
                ],id='filtro_04',className='filtros')


