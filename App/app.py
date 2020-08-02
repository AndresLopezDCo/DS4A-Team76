###########################################################################
# importar librerias generales de dash
###########################################################################

import dash
import dash_core_components as dcc
import warnings
warnings.filterwarnings('ignore')


###########################################################################
# incluir javascript
###########################################################################

external_scripts = [
    'assets/style.js'
    ,'assets/lib/bootstrap/js/bootstrap.min.js'
    ,'assets/lib/jquery/jquery.min.js'
    ,'assets/lib/jquery/jquery.dcjqaccordion.2.7.js'
    ,'assets/lib/jquery/common-scripts.js'
    ,'assets/lib/gritter/js/jquery.gritter.js'
    ,'assets/lib/gritter-conf.js'
    ,'assets/lib/chart-master/Chart.js'
]

###########################################################################
# incluir hojas de estilo
###########################################################################

external_stylesheets = [
    'assets/style.css'
    ,'assets/graphic_style.css'
    ,'assets/style-responsive.css'
    ,'assets/lib/bootstrap/css/bootstrap.min.css'
    ,'assets/lib/font-awesome/css/font-awesome.min.css'
    ,'assets/lib/gritter/css/jquery.gritter.css'
]

###########################################################################
# crear la aplicacion
###########################################################################

app = dash.Dash(__name__
    ,external_scripts=external_scripts
    ,external_stylesheets=external_stylesheets
)

app.title = 'CNC - ECAR' 

###########################################################################
# retornar llamada
###########################################################################

app.config.suppress_callback_exceptions = True