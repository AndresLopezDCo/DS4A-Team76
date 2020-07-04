#!/usr/bin/env python
# coding: utf-8

# In[134]:

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
#os.getcwd()


def get_data(ruta_n):
    ruta = os.chdir(ruta_n)
    lista=[arch.name for arch in os.scandir(ruta) if arch.is_file()]   
    data=pd.DataFrame()

    for i in lista:
        ids1=pd.read_excel(i)
        print(ids1.columns)
        data=pd.concat([data,ids1], ignore_index=True)
    return data


from sqlalchemy import create_engine, text

#maximum number of rows to display
#pd.options.display.max_rows = 20

DB_USERNAME = 'developers'
DB_PASSWORD = '12345678'
DB_INSTANCE = 'database-1.cmostnjfvkd6.us-east-2.rds.amazonaws.com'   # nombre de mi instancia
DB_PORT = '5432'
DB_DATA_BASE = 'cnc'

engine=create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_INSTANCE}:{DB_PORT}/{DB_DATA_BASE}', max_overflow=20)


def runQuery(sql):
    result = engine.connect().execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())

# In[135]:


query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_condec;"""  
df_empleados=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_fechas;"""  
df_fechas=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_marcador_automatico;"""  
df_marcadores=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_psicotecnica;"""  
df_psicotecnicas=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_sociodemografica;"""  
df_sociodemograficos=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_correspondencia_codigos;"""  
df_codigos=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_muestra_ecar_mensual_cuotas;"""  
df_cuotas=runQuery(query1)
query1 = """SELECT * FROM ecar_dwh.ecar_dwh_base_encuestas_efectivas;"""  
df_productividad=runQuery(query1)



#importar desde una carpeta todos los documentos de excel
# df_productividad=get_data('C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\EncuestasEfectivas')
# df_productividad['FECHA']=df_productividad['FECHA'].apply(lambda x: pd.to_datetime(x))  #le cambias las fechas
# df_productividad.head()


# In[136]:


# df_marcadores=get_data('C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\Marcadores')
# df_marcadores.head()


# # In[109]:

# # Exportar CSV 
# df_marcadores.to_csv(r'C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\Marcadores.csv', index = False)
# df_productividad.to_csv(r'C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\Productividad.csv', index = False)


# In[137]:

## Leer desde un documento de excel
# df_sociodemograficos = pd.read_excel('C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\Base sociodemográficos ECAR.xlsx')
# df_psicotecnicas= pd.read_excel('C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\Base psicotécnicas ECAR.xlsx')
# df_empleados= pd.read_excel('C:\\Users\\A.Lopez\\Downloads\\DS4A\\ProjectCNC\\codenc_anonim.xlsx')
# df_productividad.head(20)


# In[138]:


df_empleados.rename(columns={'tmk':'empleado'},inplace=True)

df_productividad=pd.merge(df_productividad,df_empleados,how="left",left_on='codenc',right_on='codenc')
df_psicotecnicas=pd.merge(df_psicotecnicas,df_empleados,how="left",left_on='codenc',right_on='codenc')
df_sociodemograficos=pd.merge(df_sociodemograficos,df_empleados,how="left",left_on='codenc',right_on='codenc')


# In[166]:


df_psicotecnicas.columns


# In[262]:


df_productividad['año']=pd.DatetimeIndex(df_productividad['fecha']).year
df_productividad['mes']=pd.DatetimeIndex(df_productividad['fecha']).month
df_productividad['semana']=pd.DatetimeIndex(df_productividad['fecha']).week
df_productividad


# In[286]:


prueba =df_productividad.groupby(
     ['empleado','año','mes']
 ).agg(
     cuenta_llamadas = ('telelink','count'),
 ).reset_index()
prueba2 =prueba.groupby(['empleado','año']).agg(
     cuenta_llamadas = ('cuenta_llamadas','sum'),
     cuenta_meses = ('mes', 'count'),
 ).reset_index()
prueba2['promedio_mes']= prueba2['cuenta_llamadas'] / prueba2['cuenta_meses']
prueba2


# In[296]:


filtro17=['2017']
prueba2017 = prueba2[prueba2['año'].isin(filtro17)]
prueba2017_1=prueba2017.sort_values('promedio_mes',ascending=False)
prueba2017_2=prueba2017_1[0:10]
prueba2017_2

#TOP 10 BEST POLLSTERS 2017
plt.figure(figsize=(12,7))
sns.barplot(y='promedio_mes',x='empleado',data=prueba2017_2, order=prueba2017_2.sort_values('promedio_mes',ascending = False).empleado)
plt.title('average calls per pollster TOP10 2017')
plt.xticks(rotation=90)
plt.xlabel("Pollster_ID", size=15)
plt.ylabel("Number of Calls", size=15)
plt.show()


# In[297]:


filtro18=['2018']
prueba2018 = prueba2[prueba2['año'].isin(filtro18)]
prueba2018_1=prueba2018.sort_values('promedio_mes',ascending=False)
prueba2018_2=prueba2018_1[0:10]
prueba2018_2

#TOP 10 BEST POLLSTERS 2017
plt.figure(figsize=(12,7))
sns.barplot(y='promedio_mes',x='empleado',data=prueba2018_2, order=prueba2018_2.sort_values('promedio_mes',ascending = False).empleado)
plt.title('average calls per pollster TOP10 2018')
plt.xticks(rotation=90)
plt.xlabel("Pollster_ID", size=15)
plt.ylabel("Number of Calls", size=15)
plt.show()


# In[295]:


filtro19=['2019']
prueba2019 = prueba2[prueba2['año'].isin(filtro19)]
prueba2019_1=prueba2019.sort_values('promedio_mes',ascending=False)
prueba2019_2=prueba2019_1[0:10]
prueba2019_2

#TOP 10 BEST POLLSTERS 2019
plt.figure(figsize=(12,7))
sns.barplot(y='promedio_mes',x='empleado',data=prueba2019_2, order=prueba2019_2.sort_values('promedio_mes',ascending = False).empleado)
plt.title('average calls per pollster TOP10 2019')
plt.xticks(rotation=90)
plt.xlabel("Pollster_ID", size=15)
plt.ylabel("Number of Calls", size=15)
plt.show()


# In[299]:


filtro20=['2020']
prueba2020 = prueba2[prueba2['año'].isin(filtro20)]
prueba2020_1=prueba2020.sort_values('promedio_mes',ascending=False)
prueba2020_2=prueba2020_1[0:10]
prueba2020_2

#TOP 10 BEST POLLSTERS 2019
plt.figure(figsize=(12,7))
sns.barplot(y='promedio_mes',x='empleado',data=prueba2020_2, order=prueba2020_2.sort_values('promedio_mes',ascending = False).empleado)
plt.title('average calls per pollster TOP10 2020')
plt.xticks(rotation=90)
plt.xlabel("Pollster_ID", size=15)
plt.ylabel("Number of Calls", size=15)
plt.show()


# In[332]:


plt.figure(figsize=(10,30))
df_psicotecnicas.columns
vars_to_plot=['competencias_organizacionales', 'cartografia', 'competencias_funcionales', 
              'ortografia', 'numeros','coherencia_entre_numeros','sumar', 
              'escritura']
for i, var in enumerate(vars_to_plot):
    plt.subplot(4,2,i+1)
    plt.hist(df_psicotecnicas[var],10)
    title_string="Histograma de " + var
    plt.ylabel('count')
    plt.title(title_string)
    plt.subplots_adjust(hspace=0.2, wspace=0.2)


# In[338]:


psicotecnicas_top17=pd.merge(df_psicotecnicas,prueba2017_2,how='inner',left_on='empleado',right_on='empleado')
psicotecnicas_top18=pd.merge(df_psicotecnicas,prueba2018_2,how='inner',left_on='empleado',right_on='empleado')
psicotecnicas_top19=pd.merge(df_psicotecnicas,prueba2019_2,how='inner',left_on='empleado',right_on='empleado')
psicotecnicas_top20=pd.merge(df_psicotecnicas,prueba2020_2,how='inner',left_on='empleado',right_on='empleado')
psicotecnicas_top=pd.concat([psicotecnicas_top17,psicotecnicas_top18,psicotecnicas_top19,psicotecnicas_top20],sort=True,axis=0,ignore_index=True)
psicotecnicas_top


# In[336]:


psicotecnicas_top.columns


# In[337]:

df_marcadores.archivo.replace('VCD','',inplace=True)
df_marcadores

# In[325]:


df_sociodemograficos.replace({'Ã±':'ñ','Ã©':'e','Ã³':'o','SociologÃ\xada':'sociologia','Danza y direcciÃ³n coreogrÃ¡fica ':                              'Danza y direccion coreografica', 'PsicÃ³logo ':'psicologia','PsicologÃ\xada':'psicologia',
                             },inplace=True)

cols=['barrio', 'educacion_formal','localidad','nombre_educacion']
for var in cols:
        df_sociodemograficos[var]=(df_sociodemograficos[var].astype(str)).str.lower()


# In[221]:


df_sociodemograficos


# In[223]:


df_day_prod_sum=df_productividad.groupby('fecha').agg({'duracion':'sum'}).reset_index()
df_day_prod_mean=df_productividad.groupby('fecha').agg({'duracion':'mean'}).reset_index()

plt.figure(figsize=(15,5))
plt.title('Duración total por día')
sns.lineplot(x='fecha',y='duracion',data=df_day_prod_sum)


# In[257]:



df_productividad.groupby('empleado').agg({'duracion':['sum','mean']})
#df_empleado_sum.sort_values('DURACION',inplace=True,ascending=False)
#df_productividad.groupby(pd.Grouper(freq='D',key='FECHA')).agg({'DURACION':'sum'}).reset_index()
#df_empleado_sum

# df_empleado_mean=df_productividad.groupby('Empleado').agg({'DURACION':'sum'})
# df_empleado_mean.sort_values('DURACION',inplace=True,ascending=False)
# display(df_empleado_sum,df_empleado_mean)


# In[58]:


plt.figure(figsize=(15,5))
plt.title('Duración promedio por día')
sns.lineplot(x='fecha',y='duracion',data=df_day_prod_mean)


# In[238]:


df_D_prod_sum=df_productividad.groupby(pd.Grouper(freq='D',key='fecha')).agg({'duracion':'sum'}).reset_index()
df_D_prod_mean=df_productividad.groupby(pd.Grouper(freq='D',key='fecha')).agg({'duracion':'mean'}).reset_index()
df_D_prod_sum


# In[61]:


plt.figure(figsize=(15,5))
plt.title('Duración total por día')
sns.lineplot(x='fecha',y='duracion',data=df_D_prod_sum)


# In[62]:


plt.figure(figsize=(15,5))
plt.title('Duración total por día')
sns.lineplot(x='fecha',y='duracion',data=df_D_prod_mean)


# In[55]:


df_month_prod_sum=df_productividad.groupby(pd.Grouper(freq='M',key='fecha')).agg({'duracion':'sum'}).reset_index()
df_month_prod_mean=df_productividad.groupby(pd.Grouper(freq='M',key='fecha')).agg({'duracion':'mean'}).reset_index()

plt.figure(figsize=(15,5))
plt.title('Duración total por día')
sns.lineplot(x='fecha',y='duracion',data=df_month_prod_sum)


# In[56]:


plt.figure(figsize=(15,5))
plt.title('Duración promedio por día')
sns.lineplot(x='fecha',y='duracion',data=df_month_prod_mean)


# In[53]:


df_month_prod=df_productividad.groupby(pd.Grouper(freq='W',key='FECHA')).agg({'DURACION':'mean'}).reset_index()

plt.figure(figsize=(15,5))
sns.lineplot(x='fecha',y='duracion',data=df_month_prod)


# In[40]:


plt.figure(figsize=(15,5))
sns.distplot(df_day_prod['duracion'])


# In[38]:


plt.figure(figsize=(15,5))
sns.distplot(df_month_prod['duracion'])


# In[ ]:





