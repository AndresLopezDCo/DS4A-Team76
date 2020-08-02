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
from lib import graficas, tablas,consultas,filtros
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
#
###############################################################################

@app.callback(
    Output('id_mes', 'options'),
    [Input('id_year', 'value')])
def set_mes_options(selected_year):
    return [{'label': i, 'value': i} for i in filtros.all_options[selected_year]]

###############################################################################
#
###############################################################################

@app.callback(
    Output('id_mes', 'value'),
    [Input('id_mes', 'options')])
def set_mes_value(available_options):
    return available_options[0]['value']


@app.callback (
    Output('id_figure_03','figure'),
    [Input('id_year','value'),
     Input('id_mes','value')]
)

def top_updater(value_year,value_mes):
    dff=graficas.df3[(graficas.df3['año']==value_year)&(graficas.df3['mes'].isin([value_mes]))]
    dff=dff.sort_values('count',ascending=True)
    fig_top = px.bar(dff.tail(10), x='count', y='codenc', height=500,labels={
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
#
###############################################################################