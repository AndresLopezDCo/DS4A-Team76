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
import warnings
warnings.filterwarnings('ignore')

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import consultas


###########################################################################
# creamos las tablas 
###########################################################################

# df = consultas.df_porc_tabla
dff=consultas.df_efec_completed[(consultas.df_efec_completed['año']==2020)&(consultas.df_efec_completed['mes']=='Enero')]


tabla_01 = html.Div ([
                    dte.DataTable(columns=[{"name": c, "id": c} for c in dff.columns],data=dff.head(10).to_dict('records'),
                        style_cell_conditional=[{'if': {'column_id': c},'textAlign': 'left'} for c in ['codenc', 'archivo']],
                        fixed_columns={'headers': True, 'data': 1},
                        style_table={'overflowY': 'scroll', 'overflowX': 'scroll','height': '400px'},
                        style_header={'backgroundColor': 'rgb(24, 65, 140)',
                                      'color': 'white','text-align': 'center',
                                      'font-family': 'Ruda, sans-serif','margin': '5px'},
                        style_cell={'minWidth': '60px','color': 'black','font-family': 'Ruda, sans-serif'},
                        style_as_list_view=True,id='id_table_01')
                ],id='tabla_01')



