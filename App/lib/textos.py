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
import os
import math
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text

###########################################################################
# referenciamos py externos
###########################################################################

from app import app

###########################################################################
# creamos los textos
###########################################################################

texto_01 = dcc.Markdown ('''
                            Esto es un ejemplo del texto 1 y viene la descripcion de la regresión lineal
                        ''',id='texto_01',className='texto')
texto_02 = dcc.Markdown ('''
                            Grafica 02 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 02 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 02 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 02 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 02 Este es un ejemplo acerca del detalle de las graficas
                        ''',id='texto_02',className='texto')
texto_03 = dcc.Markdown ('''
                            Grafica 03 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 03 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 03 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 03 Este es un ejemplo acerca del detalle de las graficas
                            Grafica 03 Este es un ejemplo acerca del detalle de las graficas
                        ''',id='texto_03',className='texto')

texto_04 = dcc.Markdown ('''
                            Esto es un ejemplo del texto 4 y viene la descripcion de la regresión lineal en box plot
                        ''',id='texto_04',className='texto')