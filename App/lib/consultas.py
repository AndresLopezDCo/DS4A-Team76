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
import sklearn
from math import pi

###########################################################################
# referenciamos py externos
###########################################################################

from app import app
from lib import conexion

###########################################################################
# realizar query de consultas
###########################################################################

##################################################################################################
#   Consultqa - Top numero de llamadas efectivas por estrato - genero y edad
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
#   Consulta añadir departamento para el mapa
##################################################################################################
df_efectivas['dpto']="vacio"

lista1=['Cali', 'Neiva', 'Pasto', 'Bucaramanga', 'Bogotá', 'Ibagué',
       'Cúcuta', 'Pereira', 'Medellín', 'Armenia', 'Manizales',
       'Villavicencio', 'Cartagena', 'Barranquilla', 'Montería',
       'Popayán', 'Santa Marta', 'Tunja']
lista2=['VALLE DEL CAUCA','HUILA','NARIÑO','SANTANDER','SANTAFE DE BOGOTA D.C',
       'TOLIMA','NORTE DE SANTANDER','RISARALDA','ANTIOQUIA','QUINDIO','CALDAS',
       'META','BOLIVAR','ATLANTICO','CORDOBA','CAUCA','MAGDALENA','BOYACA']

for i,j in zip(lista1,lista2):
    df_efectivas.loc[df_efectivas['Ciudad']==i,['dpto']]=j

df_mapa=np.round(df_efectivas.groupby('dpto').agg({'codenc':'count','duracion':'mean'}).reset_index().rename(columns={'codenc':'N_Efectivas'}))

df_mapa['duracion']=df_mapa['duracion'].astype(int)
##################################################################################################
#   Consultqa -Efectividad vs llamadas, duración total, espera, hablado..
##################################################################################################

query_02=""" select * from ecar_dwh.ecar_dwh_base_modelo """
df_modelo=conexion.runQuery(query_02)

cols=['calls', 'total', 'espera', 'hablado', 'disponible', 'pausas',
       'muerto', 'duracion_efectivas','efectividad_ajustada']

df_tiempos=df_modelo[cols]

##################################################################################################
#   Consultqa - Random Forest
##################################################################################################

objecto = pd.read_pickle('../data/Drforest.pickle')

# query_basetest=""" select * from ecar_dwh.ecar_dwh_base_test;"""
# X_test = conexion.runQuery(query_basetest)
# y_pred=objecto.predict(X_test)

cols=['calls', 'espera', 'hablado', 'disponible', 'pausas', 'muerto' ,'duracion_efectivas', 'dias_trabajados', 
      'meses_trabajados','competencias_funcionales','numeros', 'lectura_voz_alta','fluidez_lectura', 
      'cartografia', 'competencias_organizacionales', 'sumar', 'coherencia_entre_numeros',
      'como_conocio_cnc_internet_computrabajo_com','como_conocio_cnc_internet_pagina_web_del_cnc',
      'como_conocio_cnc_otros','como_conocio_cnc_voz_a_vozreferido_por_un_conocido','localidad_centro_oriente',
      'localidad_norte', 'localidad_otros','localidad_sur', 'localidad_sur_occidente',
      'educacion_formal_bachiller', 'educacion_formal_profesional','educacion_formal_tecnólogo', 
      'educacion_formal_técnico','estado_educacion_actualmente', 'estado_educacion_aplazado',
      'estado_educacion_culminado', 'nombre_educacion_ciencias_administrativas_y_contables',
      'nombre_educacion_ciencias_ambientales_y_salud','nombre_educacion_otros']


importances = objecto.feature_importances_
indices = np.argsort(importances)[::-1]
names = [cols[i] for i in indices]
datos_importances=pd.DataFrame({'covar': names, 'coef': importances[indices]})

##################################################################################################
#   Consulta - Cluster
##################################################################################################

query_basecluster=""" select * from ecar_dwh.ecar_dwh_base_closter;"""
df_cluster = conexion.runQuery(query_basecluster)

df_radar = pd.crosstab(df_cluster['cluster'], df_cluster['educacion_formal'])
df_radar.columns=['Bachiller', 'No_disponible', 'Profesional', 'Tecnologo', 'Tecnico']
df_radar=df_radar.reset_index()
print(df_radar.shape)
df_radar.head()
# number of variable
categories=list(df_radar)[1:]




##################################################################################################
#   Consulta - Top 10 Filtro de Año y Mes en Tabla y grafico 3 (Top 10)
##################################################################################################
query_efec_completed= """select * from ecar_dwh.ecar_dwh_base_top;"""
df_efec_completed = conexion.runQuery(query_efec_completed)
df_efec_completed=df_efec_completed.sort_values('count',ascending=False)
df_efec_completed.columns=['codenc', 'año', 'mes', 'count', 'dias_trabajados',
       'meses_trabajados', 'duracion', 'calls', '% espera', '% hablado',
       '% disponible', '% pausas', '% muerto',
       'competencia_funcionales', 'competencia_organizacionales',
       'como_conocio_cnc', 'age', 'localidad', 'educacion_formal',
       'estado_educacion', 'nombre_educacion']




