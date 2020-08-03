###########################################################################
# importar librerias generales de dash
###########################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate


import json
import certifi
import ssl
import requests
from sqlalchemy import create_engine, text
from urllib.request import urlopen
###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################
from math import pi
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import plotly.graph_objects as go 
import plotly.express as px
import pathlib
import warnings
warnings.filterwarnings('ignore')

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from about import page_1_layout
from models import page_2_layout
from info import page_3_layout
from dashboard import index_page
from lib import filtros, graficas, mapas, tablas, consultas
###########################################################################
# creamos callbacks
###########################################################################

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    else:
        return index_page
    
###############################################################################
#
###############################################################################
# with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
#     countries = json.load(response)

@app.callback (
    Output('id_mapa_col','children'),
    [Input('id_flt_mapa_01','value')]
)
def mapa_updater(value_var):
    
    countries=mapas.countries
    df_mapas=consultas.df_mapa
    if value_var=='N_Efectivas':
        labelgrap="# efec"
    else:
        labelgrap="Durac"
    for loc in countries['features']:
        loc['id'] = loc['properties']['NOMBRE_DPT']
    trace_1 = go.Choroplethmapbox(
                        geojson=countries,
                        locations=df_mapas['dpto'],
                           z=df_mapas[value_var],
                           colorscale='ylgnbu',# zmin=0, zmax=12,
                           marker_opacity=0.5, marker_line_width=0)
    layout = go.Layout(mapbox_style="carto-positron",height=700,width=550,
                  mapbox_zoom=5, mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                  margin={"r":0,"t":0,"l":0,"b":0})
   
    fig = go.Figure(data = [trace_1], layout = layout)
    map_fig=[dcc.Graph(figure=fig, id='id_map')]
    return map_fig


###############################################################################
#
###############################################################################
    
@app.callback (
    Output('id_figure_01','figure'),
    [Input('id_efectivas_cuotas','value')]
)
def cuotas_updater(value_var):
    dff=graficas.df1[graficas.df1['variable']==value_var]
    fig_efectivas_cuotas = px.bar(dff, x=dff.index, y='count', height=400,labels={
                     'index':str(value_var),
                     'count': "Cantidad de llamadas"})
    return fig_efectivas_cuotas

###############################################################################
#
###############################################################################

@app.callback (
    Output('id_figure_02','figure'),
    [Input('id_marcador','value')]
)
def marcador_updater(value_var1):
    fig_marcador = px.scatter(graficas.df2, x=value_var1, y='efectividad_ajustada', height=400)
    return fig_marcador

###############################################################################
#  Filtro por año y mes
###############################################################################

@app.callback(
    Output('id_mes', 'options'),
    [Input('id_year', 'value')])
def set_mes_options(selected_year):
    return [{'label': i, 'value': i} for i in filtros.all_options[selected_year]]


@app.callback(
    Output('id_mes', 'value'),
    [Input('id_mes', 'options')])
def set_mes_value(available_options):
    return available_options[0]['value']

###############################################################################
#  Filtro por cantidad de llamadas
###############################################################################

@app.callback (
    Output('id_figure_03','figure'),
    [Input('id_year','value'),
     Input('id_mes','value')]
)

def top_updater(value_year,value_mes):
    dff=graficas.df3[(graficas.df3['año']==value_year)&(graficas.df3['mes'].isin([value_mes]))]
    dff=dff.sort_values('count',ascending=True)
    fig_top = px.bar(dff.tail(10), x='count', y='codenc', height=400,labels={
                     'count':'Cantidad de llamadas efectivas',
                     'codenc':'Encuestador'}, color ='count',
                     color_continuous_scale=px.colors.diverging.BrBG).update_layout(coloraxis_colorbar=dict(title="count"))
    return fig_top

###############################################################################
#  
###############################################################################

@app.callback (
    Output('id_table_01','data'),
    [Input('id_year','value'),
     Input('id_mes','value')]
)

def top_updater(value_year1,value_mes1):
    dff1=consultas.df_efec_completed[
        (consultas.df_efec_completed['año']==value_year1)&(consultas.df_efec_completed['mes']==value_mes1)]
    dff1=dff1.sort_values('count',ascending=False)
    data=dff1.head(10).to_dict('records')
    return data

###############################################################################
#  Cluster - Efectivadad ajustada modifica tiempos de marcador
###############################################################################

@app.callback (
    Output('id_figure_05','figure'),
    [Input('id_marcador','value')]
)
def cluster_updater(value_var2):
    fig_cluster = px.scatter(graficas.df5, x=value_var2, y='efectividad_ajustada', height=400, color = 'cluster')
    return fig_cluster

###############################################################################
#  Radar - Filtra por cluster
###############################################################################

@app.callback (
    Output('id_figure_06','figure'),
    [Input('id_cluster','value')]
)
def cluster_updater(value_var3):
    df6=consultas.df_radar
    N = len(consultas.categories)
    values=df6.loc[value_var3].drop(['cluster']).values.flatten().tolist()
    values += values[:1]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], consultas.categories, color='grey', size=15)
    ax.set_rlabel_position(0)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    fig_radar = ax
    return fig_radar


