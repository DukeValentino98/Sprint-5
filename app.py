#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

# Vision general de datos

df.info()

df.head(10)

# Preprocesamiento de datos

df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d') # Convirtiendo fechass al tipo de datos datetime
df.isna().sum() # Obtencion de un recuento de los valores que faltan por columnda

# La columna is_4wd parece contener el valor de 1.0 si el vehículo estaba anunciado con tracción en las cuatro ruedas, y un valor faltante si no. Esto se confirmará para obtener los valores únicos, incluyendo los faltantes de esta columna, y si solo hay los dos valores mencionados anteriormente, reemplazaremos los valores faltantes con 0 (cero) y los convertiremos a enteros para actuar como un verdadero o falso booleano, 1 = verdadero, 0 = falso. Esto no significa que todos los vehículos listados con un 0 (cero) no tengan tracción en las cuatro ruedas, sino que no estaban anunciados para tenerla.

df['is_4wd'].value_counts(dropna=False)

df['is_4wd'] = df['is_4wd'].fillna(0)
df = df.astype({'is_4wd':'int64'})
df['is_4wd'].value_counts(dropna=False)

makemodel = df["model"].str.split(" ", n = 1, expand = True)
df['make'] = makemodel[0]
df['model'] = makemodel[1]
df.rename(columns={'model_year':'year', 'paint_color':'color'}, inplace=True)
df = df[['price', 'year', 'make', 'model', 'condition', 'cylinders', 'fuel','odometer', 'transmission', 'type', 'color', 'is_4wd', 'date_posted', 'days_listed']]

# Codigo Streamlit

st.header('Exploratory Analysis of Auto Listings')
st.write('''
The goal of this exploratory analysis is to use the interactive displays provided to assess trends and/or patterns relating to the listing of automobiles posted to be sold.
''')
st.write('''
Default display of vehicles only includes those listed for 30 days or less. In order to see all listings, including those listed for more than 30 days, click the checkbox below.
''')
old_listings = st.checkbox('Show cars listed over 30 days')

# Casilla para incluir vehiculos publicados por mas de 30 dias.
if not old_listings:
    df = df[df.days_listed<=30]


# Histograma para el precio(y) basado en el año(x) (deslizador para el año)

# Caja de seleccion para el histograma
hist_list = ['condition', 'fuel', 'transmission', 'type', 'is_4wd']
hist_select = st.selectbox('Filter for average price', hist_list)

# Deslizador para el año, limita el deslizador
min_year, max_year = int(df['year'].min()), int(df['year'].max())

year_range = st.slider(
    'Choose years',
    value=(min_year, max_year), min_value=min_year, max_value=max_year )

year_act_range = list(range(year_range[0],year_range[1]+1))
year_df = df[(df.year.isin(list(year_act_range)))]

fig1 = px.histogram(year_df, x='year', y='price', histfunc='avg', color=hist_select)

fig1.update_layout(title='<b>Average Price by Year</b>')

st.plotly_chart(fig1)

fig1.show()

# Gráfico de dispersión para el odómetro (y) basado en el precio (x) (con control deslizante para el precio)

# Deslizador para el grafico de dispersion
scat_list = ['condition', 'fuel', 'transmission', 'type', 'is_4wd']
scat_select = st.selectbox('Filter for mileage by price', scat_list)

# Deslizador para el precio, limita el deslizador
min_price, max_price = int(df['price'].min()), int(df['price'].max())

price_range = st.slider(
    'Set price range',
    value=(min_price, max_price), min_value=min_price, max_value=max_price )

price_act_range = list(range(price_range[0],price_range[1]+1))
price_df = df[(df.price.isin(list(price_act_range)))]

fig2 = px.scatter(price_df, x='price', y='odometer', color=scat_select)

fig2.update_layout(title='<b>Mileage by Price (USD)</b>')

st.plotly_chart(fig2)

fig2.show()

# Diagrama de caja para el odómetro (y) basado en los cilindros (con control deslizante para los cilindros)

# Caja de seleccion para el diagrama de caja
box_list = ['condition', 'fuel', 'transmission', 'type', 'is_4wd']
box_select = st.selectbox('Filter for mileage by cylinder count', box_list)

# Deslizador del cilindraje, limita el deslizador
min_cyl, max_cyl = int(df['cylinders'].min()), int(df['cylinders'].max())

cyl_range = st.slider(
    'Specify number of cylinders',
    value=(min_cyl, max_cyl), min_value=min_cyl, max_value=max_cyl )

cyl_act_range = list(range(cyl_range[0],cyl_range[1]+1))
cyl_df = df[(df.cylinders.isin(cyl_act_range))]

fig3 = px.box(cyl_df, x='cylinders', y='odometer', color=box_select)

fig3.update_layout(title='<b>Distribution of Mileage by Cylinder Count</b>')

st.plotly_chart(fig3)

fig3.show()
