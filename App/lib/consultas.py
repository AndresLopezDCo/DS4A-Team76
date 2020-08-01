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

##################################################################################################
#   Consultqa - Top 10 Tabla
##################################################################################################
query_01= """
SELECT * FROM efectivas_final;
"""
df_efectivas = conexion.runQuery(query_01)
df_efectivas['Edad'].replace('12 a 17 años','12 a 17',inplace=True)
df_efectivas_cuotas=pd.DataFrame()
for i in ['Estrato', 'Genero','Edad']:
    df_count=df_efectivas.groupby(i)[['codenc']].count().rename(columns={'codenc':"count"})
    df_count['variable']=i
    df_efectivas_cuotas=pd.concat([df_count, df_efectivas_cuotas])
    

df_efectivas_cuotas=df_efectivas_cuotas.sort_values('count',ascending=False)

##################################################################################################
#   Consultqa - Top 10 Tabla
##################################################################################################

query_02=""" select * from ecar_dwh.ecar_dwh_base_modelo """
df_modelo=conexion.runQuery(query_02)

cols=['calls', 'total', 'espera', 'hablado', 'disponible', 'pausas',
       'muerto', 'duracion_efectivas','efectividad_ajustada']

df_tiempos=df_modelo[cols]

##################################################################################################
#   Consultqa - Top 10 Tabla
##################################################################################################
cols2=['efectivas_mujer', 'efectivas_hombre','efectivas_alto', 'efectivas_medio_alto', 'efectivas_medio_medio','efectivas_bajo', 'efectivas_medio_bajo', 'efectivas_tunja',
       'efectivas_popayán', 'efectivas_montería', 'efectivas_manizales','efectivas_armenia', 'efectivas_villavicencio', 'efectivas_pasto','efectivas_cúcuta', 'efectivas_santa_marta', 'efectivas_ibagué',
       'efectivas_neiva', 'efectivas_pereira', 'efectivas_cartagena','efectivas_cali', 'efectivas_bucaramanga', 'efectivas_barranquilla','efectivas_medellín', 'efectivas_bogotá', 'efectivas_rango_edad_5',
       'efectivas_rango_edad_2', 'efectivas_rango_edad_4','efectivas_rango_edad_3', 'efectivas_rango_edad_1']
df_modelo=df_modelo[df_modelo['codenc']!='Encuestador 290']
for i in cols2:
    df_modelo["%" + str(i)]=round((df_modelo[i]/df_modelo['efectividad_ajustada'])*100).astype(int)
    
df_modelo['efectividad_ajustada']=round(df_modelo['efectividad_ajustada']).astype(int)
df_porc_tabla=df_modelo[['codenc','efectividad_ajustada','meses_trabajados','como_conocio_cnc','localidad','educacion_formal','estado_educacion','nombre_educacion',
         '%efectivas_mujer', '%efectivas_hombre', '%efectivas_alto','%efectivas_medio_alto', '%efectivas_medio_medio',
         '%efectivas_bajo', '%efectivas_medio_bajo','%efectivas_tunja', '%efectivas_popayán','%efectivas_montería', 
         '%efectivas_manizales','%efectivas_armenia', '%efectivas_villavicencio','%efectivas_pasto', '%efectivas_cúcuta',
         '%efectivas_santa_marta', '%efectivas_ibagué','%efectivas_neiva', '%efectivas_pereira','%efectivas_cartagena', '%efectivas_cali',
         '%efectivas_bucaramanga', '%efectivas_barranquilla','%efectivas_medellín', '%efectivas_bogotá','%efectivas_rango_edad_5', '%efectivas_rango_edad_2',
         '%efectivas_rango_edad_4', '%efectivas_rango_edad_3','%efectivas_rango_edad_1']]

df_porc_tabla=df_porc_tabla.sort_values('efectividad_ajustada',ascending=False)

#----------------------------------------------------------------------------------------------------------
df_efectivas['mes']= pd.DatetimeIndex(df_efectivas['fecha']).month
df_efectivas['dia']= pd.DatetimeIndex(df_efectivas['fecha']).day
df_efectivas['año']= pd.DatetimeIndex(df_efectivas['fecha']).year
df_efectivas_groupm=df_efectivas.groupby(['codenc','mes','año']).agg({'Edad':'count'}).reset_index().rename(columns={'Edad':'count'})
df_efectivas_groupm=df_efectivas_groupm.sort_values('count',ascending=False)



# query_01 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 10;"""
# df_ejemplo_01 = conexion.runQuery(query_01)

# query_02 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 20;"""
# df_ejemplo_02 = conexion.runQuery(query_02)
