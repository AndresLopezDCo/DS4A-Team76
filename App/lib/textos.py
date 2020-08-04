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
                            301
                        ''',id='id_texto_01',className='etiqueta')
descripcion_01 = dcc.Markdown ('''
                            ENCUESTADORES
                        ''',id='id_descripcion_01',className='descripcion')
texto_02 = dcc.Markdown ('''
                            12%
                        ''',id='id_texto_02',className='etiqueta')
descripcion_02 = dcc.Markdown ('''
                            EFECTIVIDAD 
                        ''',id='id_descripcion_02',className='descripcion')
texto_03 = dcc.Markdown ('''
                            4
                        ''',id='id_texto_03',className='etiqueta')
descripcion_03 = dcc.Markdown ('''
                            MESES TRABAJADOS PROM
                        ''',id='id_descripcion_03',className='descripcion')
texto_04 = dcc.Markdown ('''
                            241
                        ''',id='id_texto_04',className='etiqueta')
descripcion_04 = dcc.Markdown ('''
                            (Me) LLAMADAS EFECTIVAS 
                        ''',id='id_descripcion_04',className='descripcion')
texto_05 = dcc.Markdown ('''
                            62%
                        ''',id='id_texto_05',className='etiqueta')
descripcion_05 = dcc.Markdown ('''
                            ACCURACY RANDOM FOREST
                        ''',id='id_descripcion_05',className='descripcion')
texto_06 = dcc.Markdown ('''
                            4
                        ''',id='id_texto_06',className='etiqueta')
descripcion_06 = dcc.Markdown ('''
                            NUMERO DE CLUSTERS
                        ''',id='id_descripcion_06',className='descripcion')
texto_07 = dcc.Markdown ('''
                            30%
                        ''',id='id_texto_07',className='etiqueta')
descripcion_07 = dcc.Markdown ('''
                            MÁS EFECTIVOS (BACHILLERES)-Cluster 0
                        ''',id='id_descripcion_07',className='descripcion')
texto_08 = dcc.Markdown ('''
                            91%
                        ''',id='id_texto_08',className='etiqueta')
descripcion_08 = dcc.Markdown ('''
                            MENOS EFECTIVOS (NO BACHILLER)-Cluster 3
                        ''',id='id_descripcion_08',className='descripcion')
about_01 = dcc.Markdown ('''
                            Ingeniero en ciencia de materiales y metalurgia, con más de dos (2) años de experiencia en gestión de información, análisis de elementos finitos e integridad de activos en el sector energético
                        ''',id='id_about_01',className='about_text')
about_02 = dcc.Markdown ('''
                            Estadística y Magíster en Modelado & Simulación con más de siete (7) años de experiencia en investigación de mercados y desarrollo de modelos analíticos
                        ''',id='id_about_02',className='about_text')
about_03 = dcc.Markdown ('''
                            Matemática y Magíster en estadística con más de dos (2) años de experiencia en análisis de datos, modelos predictivos y descriptivos e inteligencia artificial.
                        ''',id='id_about_03',className='about_text')
about_04 = dcc.Markdown ('''
                            Economista y Magíster en Finanzas con más de siete (7) años de experiencia en finanzas, inteligencia de mercados y analitica de negocios
                        ''',id='id_about_04',className='about_text')
about_05 = dcc.Markdown ('''
                            Ingeniero de Sistemas Especialista en Gerencia de Proyectos en Inteligencia de Negocios con más de quince (15) años de experiencia en BI, PMP y Analitica. 
                        ''',id='id_about_05',className='about_text')
informacion_01 = dcc.Markdown ('''
                            Aqui aparecerá el Logo del Centro Nacional de Consultoria con el fin de identificar nuestro cliente externo, así mismo podemos dar clic en el con el fin
                            de poder dirigirnos al dashboard
                        ''',id='id_info_01',className='about_text')
informacion_02 = dcc.Markdown ('''
                            Aqui podemos encontrar unos botones que permitiran visualizar los resultados de los modelos (modelos), 
                            junto con una descripción acerca del equipo de trabajo (acerca team76) en donde podran visualizar los perfiles de los cientificos de datos,
                            al igual puedes ingresar nuevamente a el dashboard (dashboard) en cualquier momento.
                        ''',id='id_info_02',className='about_text')
informacion_03 = dcc.Markdown ('''
                            Permite al usuario elegir la variable que quiere consultar en el mapa para la ver la distribución por departamento. Opciones: llamadas efectivas, duración llamadas, numero de cuotas, porcentaje de llamadas efectivas sobre el total de llamadas
                        ''',id='id_info_03',className='about_text')
informacion_04 = dcc.Markdown ('''
                            Modifica la visualización del grafico “llamadas efectivas” para que el usuario puede ver la distribución de las llamadas efectivas. Opciones: estrato, genero, edad del encuestado
                        ''',id='id_info_04',className='about_text')
informacion_05 = dcc.Markdown ('''
                            Modifica la visualización del grafico “efectividad vs tiempos” para que el usuario puede ver la relación entre efectividad y las diferentes variables de la base de marcador automático. Opciones: Duración hablado, total llamadas, Duración total, Duración espera, Duración hablado, Duración disponible, Duración pausas 
                        ''',id='id_info_05',className='about_text')
informacion_06 = dcc.Markdown ('''
                            Permite al usuario elegir el periodo en el que quiere consultar el top 10 de encuestadores con más llamadas efectivas (tanto el grafico, como la tabla con las características)
                        ''',id='id_info_06',className='about_text')
informacion_07 = dcc.Markdown ('''
                            En este mapa interactivo el usuario puede ver la distribución por ciudad de país de las diferentes variables de interés (llamadas efectivas, duración llamadas, numero de cuotas, porcentaje de llamadas efectivas sobre el total de llamadas) 
                        ''',id='id_info_07',className='about_text')
informacion_08 = dcc.Markdown ('''
                            Este grafico de barras muestra la distribución de las llamadas efectivas de acuerdo a diferentes características del publico encuestado (estrato, genero, edad), el grafico cambia de acuerdo a la variable que se desee consultar y que se seleccione en el filtro “VARIABLE” 
                        ''',id='id_info_08',className='about_text')
informacion_09 = dcc.Markdown ('''
                            En este grafico el usuario puede ver la relación entre la efectividad (llamadas efectivas) y las diferentes variables de la base de marcador automático (duración total, tiempo hablado, tiempo en espera, tiempo disponible, tiempo muerto), el grafico cambia de acuerdo a la variable de marcador que se desee consultar y que se seleccione en el filtro 
                        ''',id='id_info_09',className='about_text')
informacion_10 = dcc.Markdown ('''
                            Este grafico muestra de mayor a menor el top de encuestadores que realizaron más llamadas en un periodo determinado, para elegir qué periodo se quiere consultar el usuario debe elegir el año y el mes del filtro “Año” en la sección de filtros 
                        ''',id='id_info_10',className='about_text')
informacion_11 = dcc.Markdown ('''
                            Esta tabla muestra las principales características de los encuestadores mostrados en el top 10 (de acuerdo con la informacion compartida por la entidad)
                        ''',id='id_info_11',className='about_text')
informacion_12 = dcc.Markdown ('''
                            se puede acceder a los diferentes filtros que afectan las gráficas y la información presentada
                        ''',id='id_info_12',className='about_text')
informacion_13 = dcc.Markdown ('''
                            aqui se detallan los principales indicadores (kpi) de conformidad con el analisis exploratorio de datos (eda)
                        ''',id='id_info_12',className='about_text')
informacion_14 = dcc.Markdown ('''
                            se puede acceder a los diferentes filtros que afectan las gráficas y la información presentada
                        ''',id='id_info_12',className='about_text')