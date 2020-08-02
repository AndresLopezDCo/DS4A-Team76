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

###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################

import pathlib
import math
import numpy as np
import datetime as dt
import pandas as pd
import json
import requests
import plotly.graph_objects as go 
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import filtros, textos, graficas, interacciones , mapas , tablas


###########################################################################
# crear contenido html
###########################################################################
app.layout = html.Section([
    #######################################################################
    # cabecera
    #######################################################################
    html.Header ([
        html.Div ([
            html.Div ([],className='fa fa-bars tooltips')
        ],className='sidebar-toggle-box'),
        html.A ([
            html.B ([
                'CNC'
                ,html.Span (' ECAR')
            ])
        ],href='',className='logo')
    ],className='header black-bg')
    #######################################################################
    # sidebar
    #######################################################################
    ,html.Aside ([
        html.Div ([
            html.Ul ([
                html.P ([
                    html.Img(src='assets/usuario.jpg', className='img-circle logo')
                ],className='centered')
                ,html.H5('TEAM76', className='centered')
                ,html.Li([
                    html.A ([
                        html.I(className='fa fa-bar-chart-o')
                        ,html.Span('DASHBOARD')
                    ], href='', className='active')
                ], className='mt')
                ###########################################################
                # filtros
                ###########################################################
                ,filtros.filtro_01   #mapa
                ,filtros.filtro_02   #efectividad - cuotas
                ,filtros.filtro_03   #Tiempos - Marcador
                ,filtros.filtro_04   #Filtro de año
#                 ,filtros.filtro_05   #Filtro de mes
                ,filtros.filtro_06   #Slider
#                 ,filtros.filtro_1001 # prueba caalbacks
            ],id='nav-accordion', className='sidebar-menu')
        ],id='sidebar', className='nav-collapse ')
    ])
    ,html.Section ([
        html.Section ([
            ###############################################################
            # contenido
            ###############################################################
            html.Div ([
                ###########################################################
                    # tarjeta 1
                ###########################################################
                html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_01
                    ,textos.descripcion_01
                ],className='col-md-3 tarjetas color_01')
                ###########################################################
                    # tarjeta 2
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_02
                    ,textos.descripcion_02
                ],className='col-md-3 tarjetas color_02')
                ###########################################################
                    # tarjeta 3
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_03
                    ,textos.descripcion_03
                ],className='col-md-3 tarjetas color_03')
                ###########################################################
                    # tarjeta 4
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_04
                    ,textos.descripcion_04
                ],className='col-md-3 tarjetas color_04')
            ],className='row')
            ,html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('ESTADISTICAS POR DEPARTAMENTO')
                    ],className='border-head')
                    #######################################################
                    # mapa de colombia "mapa 1", descripción "texto 5"
                    #######################################################
                    ,mapas.mapa_01
                ],className='col-md-6 main-chart')
                ,html.Div ([
                    html.Div ([
                        html.Div ([
                            html.Div ([
                                html.H3('LLAMADAS EFECTIVAS')
                            ],className='border-head')
                            #######################################################
                            # grafica 1 y texto 6
                            #######################################################
                             ,graficas.grafica_01
                        ],className='col-md-12 main-chart')
                        ,html.Div ([
                            html.Div ([
                                html.H3('EFECTIVIDAD vs. TIEMPOS')
                            ],className='border-head')
                            #######################################################
                            # grafica 2 y texto 7
                            #######################################################
                            ,graficas.grafica_02
                        ],className='col-md-12 main-chart')
                    ],className='row')
                ],className='col-md-6 main-chart')
            ],className='row')
            ,html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('TOP 10 ENCUESTADORES')
                    ],className='border-head')
                    #######################################################
                    # grafica 3 y texto 8
                    #######################################################
                    ,graficas.grafica_03
                ],className='col-md-6 main-chart')
                ,html.Div ([
                    html.Div ([
                        html.H3('DETALLE DE ENCUESTADORES')
                    ],className='border-head')
                    #######################################################
                    # grafica 3 y texto 3
                    #######################################################
                     ,tablas.tabla_01
                ],className='col-md-6 main-chart')
            ],className='row')
            ,html.Div ([
                ###########################################################
                    # tarjeta 5
                ###########################################################
                html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_05
                    ,textos.descripcion_05
                ],className='col-md-3 tarjetas color_05')
                ###########################################################
                    # tarjeta 6
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_06
                    ,textos.descripcion_06
                ],className='col-md-3 tarjetas color_06')
                ###########################################################
                    # tarjeta 7
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_07
                    ,textos.descripcion_07
                ],className='col-md-3 tarjetas color_07')
                ###########################################################
                    # tarjeta 8
                ###########################################################
                ,html.Div ([
                    html.Img(src='assets/logo_02.png', className='icono')
                    ,textos.texto_08
                    ,textos.descripcion_08
                ],className='col-md-3 tarjetas color_08')
            ],className='row')
        ],className='wrapper')
        ###################################################################
        # pie de pagina
        ###################################################################
        ,html.Footer ([
            html.Div ([
                html.P ([
                    'Copyright 2020'
                    ,html.Strong(' CNC ')
                    ,'Todos los derechos reservados'
                ])
                ,html.A ([
                    html.I ([
                    ],className='fa fa-angle-up')
                ],href='index.py#', className='go-top')
            ],className='text-center')
        ],className='site-footer')
    ],id='main-content')
],id='container')

###########################################################################
# inicializar el servidor
###########################################################################

if __name__ == "__main__":
    app.run_server(host='127.0.0.1',port=8050, debug=True)