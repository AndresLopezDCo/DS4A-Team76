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
# referenciamos py externos
###########################################################################

from app import app
from about import page_1_layout
from models import page_2_layout
from info import page_3_layout
from dashboard import index_page
from lib import paginas


###########################################################################
# crear contenido html
###########################################################################
app.layout = html.Section([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
],id='container')

###########################################################################
# inicializar el servidor
###########################################################################

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port=8050, debug=True)