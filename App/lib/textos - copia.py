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
                            1000
                        ''',id='id_texto_01',className='etiqueta')
descripcion_01 = dcc.Markdown ('''
                            DESCRIPCION 1
                        ''',id='id_descripcion_01',className='descripcion')
texto_02 = dcc.Markdown ('''
                            500
                        ''',id='id_texto_02',className='etiqueta')
descripcion_02 = dcc.Markdown ('''
                            DESCRIPCION 2
                        ''',id='id_descripcion_02',className='descripcion')
texto_03 = dcc.Markdown ('''
                            700
                        ''',id='id_texto_03',className='etiqueta')
descripcion_03 = dcc.Markdown ('''
                            DESCRIPCION 3
                        ''',id='id_descripcion_03',className='descripcion')
texto_04 = dcc.Markdown ('''
                            1200
                        ''',id='id_texto_04',className='etiqueta')
descripcion_04 = dcc.Markdown ('''
                            DESCRIPCION 4
                        ''',id='id_descripcion_04',className='descripcion')

