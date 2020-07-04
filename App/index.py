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
from lib import filtros, textos, graficas


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
        ],href='index.py',className='logo')
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
                ,html.H5('CAMILO AMEZQUITA', className='centered')
                ,html.Li([
                    html.A ([
                        html.I(className='fa fa-bar-chart-o')
                        ,html.Span('DASHBOARD')
                    ], href='index.py', className='active')
                ], className='mt')
                ###########################################################
                # filtros
                ###########################################################
                ,filtros.filtro_01
                ,filtros.filtro_02
            ],id='nav-accordion', className='sidebar-menu')
        ],id='sidebar', className='nav-collapse ')
    ])
    ,html.Section ([
        html.Section ([
            ###############################################################
            # contenido
            ###############################################################
            html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('DISTRIBUCIÓN POR RANGO DE EDAD')
                    ],className='border-head')
                    #######################################################
                    # grafica 1 y texto 1
                    #######################################################
                    ,graficas.grafica_01
                    ,textos.texto_01
                ],className='col-md-12 main-chart')
            ],className='row')
            ,html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('DISTRIBUCIÓN EJEMPLO')
                    ],className='border-head')
                    #######################################################
                    # grafica 4 y texto 4
                    #######################################################
                    ,graficas.grafica_04
                    ,textos.texto_04
                ],className='col-md-12 main-chart')
            ],className='row')
            ,html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('DISTRIBUCIÓN POR RANGO DE EDAD')
                    ],className='border-head')
                    #######################################################
                    # grafica 2 y texto 2
                    #######################################################
                    ,graficas.grafica_02
                    ,textos.texto_02
                ],className='col-md-6 main-chart')
                ,html.Div ([
                    html.Div ([
                        html.H3('DISTRIBUCIÓN POR RANGO DE EDAD')
                    ],className='border-head')
                    #######################################################
                    # grafica 3 y texto 3
                    #######################################################
                    ,graficas.grafica_03
                    ,textos.texto_03
                ],className='col-md-6 main-chart')
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