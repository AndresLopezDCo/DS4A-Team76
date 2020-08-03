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
                            {'label': 'Llamadas efectivas', 'value': 'N_Efectivas'}
                            ,{'label': 'Duración promedio', 'value': 'duracion'}
                        ],id='id_flt_mapa_01',value='N_Efectivas')
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
                            ,{'label': 'Edad', 'value': 'Edad'}
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
# creamos filtro de Top 10 por año
###########################################################################

all_options = {
                2017:['Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                2018:['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                    'Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                2019:['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                    'Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                2020:['Enero','Febrero','Marzo']
                     }
filtro_04=html.Div (children=[
                    html.Label('AÑO', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                           {'label': k, 'value': k} for k in all_options.keys()
                        ],id='id_year',value=2020)
                    ,dcc.Dropdown(id='id_mes')
                ],id='filtro_04',className='filtros')

###########################################################################
# creamos filtro de Top 10 por mes
###########################################################################

filtro_05= html.Div (children=[
                    html.Label('ClUSTER', className='filtros-label')
                    ,dcc.Dropdown(
                        options=[
                            {'label': 'Cluster 0', 'value':0},
                            {'label': 'Cluster 1', 'value':1},
                            {'label': 'Cluster 2', 'value':2},
                            {'label': 'Cluster 3', 'value':3}
                        ],id='id_cluster',value=0)
                ],id='filtro_05',className='filtros')


###########################################################################
# creamos filtro de slider para modificar por mes los markdown
###########################################################################

filtro_06 = html.Div (children=[
                    html.Label('DURACIÓN [MESES]', className='filtros-label')
                    ,dcc.Slider(
                        id='my-slider',
                        min=1,
                        max=26,
                        step=1,
                        value=6,
                        #mark={1:'1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6'},
                    ), html.Div(id='id_filtro_06')
                ],id='filtro_06',className='filtros')


