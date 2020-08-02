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
from lib import consultas,filtros,graficas,tablas

###########################################################################
# creamos callbacks
###########################################################################

# @app.callback (
#     Output('id_figure_02','figure'),
#     # input es el id del filtro, valor del filtro
#     [Input('tipo_grafico_01','value')]
# )
# def callback_filtro_03(slider_value):
#     if slider_value=='1':
#         tipe_fig=graficas.fig_ejemplo1
#     elif slider_value=='2':
#         tipe_fig=graficas.fig_ejemplo2
#     elif slider_value=='3':
#         tipe_fig=graficas.fig_ejemplo3
#     elif slider_value=='4':
#         tipe_fig=graficas.fig_ejemplo4
#     else:
#         tipe_fig=graficas.fig_ejemplo1
#     return tipe_fig

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

@app.callback (
    Output('id_figure_02','figure'),
    [Input('id_marcador','value')]
)
def marcador_updater(value_var1):
    fig_marcador = px.scatter(graficas.df2, x=value_var1, y='efectividad_ajustada', height=400)
    return fig_marcador



#-----------------------------------------------------------------
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


@app.callback (
    Output('id_figure_03','figure'),
    [Input('id_year','value'),
     Input('id_mes','value')]
)
# id_figure_03
def top_updater(value_year,value_mes):
    dff=graficas.df3[(graficas.df3['año']==value_year)&(graficas.df3['mes'].isin([value_mes]))]
    dff=dff.sort_values('count',ascending=True)
    fig_top = px.bar(dff.tail(10), x='count', y='codenc', 
                     color='count', height=500,labels={
                     'count':'Cantidad de llamadas efectivas',
                     'codenc':'Encuestador'})
    return fig_top

@app.callback (
    Output('id_table_01','data'),
    [Input('id_year','value'),
     Input('id_mes','value')]
)
# id_figure_03
def top_updater(value_year1,value_mes1):
    dff1=consultas.df_efec_completed[
        (consultas.df_efec_completed['año']==value_year1)&(consultas.df_efec_completed['mes']==value_mes1)]
    dff1=dff1.sort_values('count',ascending=False)
    data=dff1.head(10).to_dict('records')
#     value=tablas.generate_table(dff1,max_rows=10)
    return data


