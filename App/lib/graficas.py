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
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text
from math import pi
###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas, filtros

###########################################################################
# creamos variables por graficas y setearlas por defecto
###########################################################################


df1 = consultas.df_efectivas_cuotas
ejex1 = df1.index
ejey1 = 'count'

df2 = consultas.df_tiempos
ejex2 = 'calls'
ejey2 = 'efectividad_ajustada'

df3=consultas.df_efec_completed
ejex3='count'
ejey3='codenc'

df4=consultas.datos_importances
ejex4='coef'
ejey4='covar'

df5=consultas.df_cluster
ejex5='calls'
ejey5='efectividad_ajustada'


df6=consultas.df_radar
N = len(consultas.categories)
values=df6.loc[3].drop(['cluster']).values.flatten().tolist()
values += values[:1]
#values
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]



ejex7='cluster'
ejey7='efectividad_ajustada'


#Graficas por defecto 
fig_efectivas_cuotas= px.bar(df1, x=ejex1, y=ejey1, height=400,labels={
                     'index':'Estrato',
                     'count':'Cantidad de llamadas'})
fig_marcador = px.scatter(df2, x=ejex2, y=ejey2, height=400)

fig_top = px.bar(df3.head(20), x=ejex3, y=ejey3, height=450,labels={
                     'count':'Cantidad de llamadas efectivas',
                     'codenc':'Encuestador'})

fig_random_forest = px.bar(df4, x=ejex4, y=ejey4,height=450,labels={
                     'coef':'Coeficiente de importancia',
                     'covar':'Covariables'})

fig_cluster = px.scatter(df5, x=ejex5, y=ejey5, color="cluster")


ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], consultas.categories, color='grey', size=15)
ax.set_rlabel_position(0)
ax.plot(angles, values, linewidth=1, linestyle='solid')
ax.fill(angles, values, 'b', alpha=0.1)
fig_radar = ax


fig_boxplot = px.box(df5, x=ejex7, y=ejey7, height=400)

###########################################################################
# grafica efectividad - cuotas por genero, genero, edad
###########################################################################


grafica_01 = html.Div ([
                    dcc.Graph(figure=fig_efectivas_cuotas,id='id_figure_01')
                ],id='id_grafica_01')

#id contenedor html 'id_grafica_01 y 'id_figura_01 es el id de la grafica

###########################################################################
# grafica distribucion por estrato barras
###########################################################################

grafica_02 = html.Div ([
                    dcc.Graph(figure=fig_marcador,id='id_figure_02')
                ],id='id_grafica_02')

###########################################################################
# grafica distribucion por estrato scatter
###########################################################################

grafica_03 = html.Div ([
                    dcc.Graph(figure=fig_top,id='id_figure_03')
                ],id='id_grafica_03')

###########################################################################
# grafica modelo por Random forest
###########################################################################

grafica_04 = html.Div ([
                    dcc.Graph(figure=fig_random_forest,id='id_figure_04')
                ],id='id_grafica_04')

###########################################################################
# grafica modelo por Cluster
###########################################################################

grafica_05 = html.Div ([
                    dcc.Graph(figure=fig_cluster,id='id_figure_05')
                ],id='id_grafica_05')

###########################################################################
# grafica modelo por Cluster
###########################################################################

grafica_06 = html.Div ([
                    dcc.Graph(figure=fig_radar,id='id_figure_06')
                ],id='id_grafica_06')

###########################################################################
# grafica modelo por Cluster
###########################################################################

grafica_07 = html.Div ([
                    dcc.Graph(figure=fig_boxplot,id='id_figure_07')
                ],id='id_grafica_07')


