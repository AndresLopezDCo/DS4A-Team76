###########################################################################
# importar librerias de manejo de archivos, operaciones y graficas
###########################################################################

import pathlib
import os
import numpy as np
import pandas as pd
import json
import warnings
warnings.filterwarnings('ignore')
from sqlalchemy import create_engine, text

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import conexion

###########################################################################
# realizar query de consultas
###########################################################################

query_01 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 10;"""
df_ejemplo_01 = conexion.runQuery(query_01)

query_02 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 20;"""
df_ejemplo_02 = conexion.runQuery(query_02)
