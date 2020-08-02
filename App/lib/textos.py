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
texto_05 = dcc.Markdown ('''
                            1000
                        ''',id='id_texto_05',className='etiqueta')
descripcion_05 = dcc.Markdown ('''
                            DESCRIPCION 1
                        ''',id='id_descripcion_05',className='descripcion')
texto_06 = dcc.Markdown ('''
                            500
                        ''',id='id_texto_06',className='etiqueta')
descripcion_06 = dcc.Markdown ('''
                            DESCRIPCION 2
                        ''',id='id_descripcion_06',className='descripcion')
texto_07 = dcc.Markdown ('''
                            700
                        ''',id='id_texto_07',className='etiqueta')
descripcion_07 = dcc.Markdown ('''
                            DESCRIPCION 3
                        ''',id='id_descripcion_07',className='descripcion')
texto_08 = dcc.Markdown ('''
                            1200
                        ''',id='id_texto_08',className='etiqueta')
descripcion_08 = dcc.Markdown ('''
                            DESCRIPCION 4
                        ''',id='id_descripcion_08',className='descripcion')
about_01 = dcc.Markdown ('''
                            Ingeniero en ciencia de materiales y metalurgia, con experiencia en gestión de información, análisis de elementos finitos e integridad de activos en el sector energético
                        ''',id='id_about_01',className='about_text')
about_02 = dcc.Markdown ('''
                            Estadística y Máster en Modelado & Simulación con +7 años de experiencia en investigación de mercados y desarrollo de modelos analíticos
                        ''',id='id_about_02',className='about_text')
about_03 = dcc.Markdown ('''
                            Aqui viene la descripcion del perfil de yesica, Aqui viene la descripcion del perfil de yesica, Aqui viene la descripcion del perfil de yesica
                        ''',id='id_about_03',className='about_text')
about_04 = dcc.Markdown ('''
                            Economista y Magister en Finanzas con más de siete (7) años de experiencia en finanzas, inteligencia de mercados y analitica de negocios
                        ''',id='id_about_04',className='about_text')
about_05 = dcc.Markdown ('''
                            Ingeniero de Sistemas Especialista en Gerencia de Proyectos en Inteligencia de Negocios con más de quince (15) años de experiencia en BI, PMP y Analitica. 
                        ''',id='id_about_05',className='about_text')