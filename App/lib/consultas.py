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

query = """SELECT * FROM ecar_dm.ejemplo;"""
df_ejemplo = conexion.runQuery(query)