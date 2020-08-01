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
select distinct tabla1.* from(
select tabla.*, cu.etiquetas_rango_edad from(
select codenc, telelink, fecha, duracion, edad,  "ciudad", "Estrato", edcc.etiqueta as "Genero", cod_rango_edad from (
select codenc, telelink, fecha, duracion, edad, "cod_ciudad", "ciudad", estrato as "cod_estrato", 
edcc.etiqueta as "Estrato", genero, cod_rango_edad  from(
select codenc, telelink, fecha, duracion, edad, ciudad as "cod_ciudad", edcc.etiqueta as "ciudad", estrato, genero, cod_rango_edad
from ecar_dwh.ecar_dwh_base_encuestas_efectivas edbee 
inner join ecar_dwh.ecar_dwh_base_correspondencia_codigos edcc on edbee.ciudad=edcc.codigo
where edcc.campo='ciudad')tt
inner join ecar_dwh.ecar_dwh_base_correspondencia_codigos edcc on tt.estrato=edcc.codigo
where edcc.campo='estrato')tt1
inner join ecar_dwh.ecar_dwh_base_correspondencia_codigos edcc on tt1.genero=edcc.codigo
where edcc.campo='genero')tabla
left join ecar_dwh.ecar_dwh_base_muestra_ecar_mensual_cuotas cu on cu.cod_rango_edad=tabla.cod_rango_edad)tabla1
"""
df_efectivas = conexion.runQuery(query_01)
df_efectivas['etiquetas_rango_edad'].replace('12 a 17 años','12 a 17',inplace=True)
df_efectivas_cuotas=pd.DataFrame()
for i in ['Estrato', 'Genero','etiquetas_rango_edad']:
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



# query_01 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 10;"""
# df_ejemplo_01 = conexion.runQuery(query_01)

# query_02 = """select * from ecar_dwh.ecar_dwh_base_encuestas_efectivas limit 20;"""
# df_ejemplo_02 = conexion.runQuery(query_02)
