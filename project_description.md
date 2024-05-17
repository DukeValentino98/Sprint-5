***Instrucciones proporcionadas por TripleTen:***

# Herramientas de desarrollo de software: Proyecto

¡Felicidades! Completaste la sección sobre herramientas de desarrollo de software. Ahora es el momento de aplicar los conocimientos y habilidades adquiridos al realizar un proyecto: construir y desplegar un panel de control de una aplicación web en un servicio en la nube.

Una vez que hayas terminado el proyecto, recuerda enviar tu trabajo al equipo de supervisión de proyectos para su evaluación. Te dará su opinión en 48 horas. Utiliza los comentarios para realizar cambios y luego envía la nueva versión al revisor.

Es posible que recibas más comentarios sobre esta nueva versión. Esto es totalmente normal. No es nada raro que pases por varios ciclos de comentarios y revisiones.

Tu proyecto se considerará completado una vez que el revisor del proyecto lo apruebe.

# Descripcion del proyecto

El objetivo de este proyecto es proporcionarte más posibilidades de practicar las tareas habituales de la ingeniería de software. Gracias a estas tareas, podrás aumentar y complementar tus habilidades en el campo de los datos y te convertirás en un candidato más atractivo para posibles empleadores.

Las tareas incluyen la creación y gestión de entornos virtuales de Python, el desarrollo de una aplicación web y su despliegue en un servicio en la nube que la hará accesible al público.

En este proyecto, te proporcionamos un conjunto de datos de anuncios de venta de coches. Sin embargo, en este proyecto, el enfoque no se centrará en el conjunto de datos ni en el análisis, por lo que eres libre de elegir cualquier dataset que desees.

Observa el aspecto que podría tener tu solución final:

[Demo de la aplicacion](https://www.youtube.com/watch?v=bna15Zj6jUI)

# Instrucciones para completar el proyecto

## Paso 1. Configuracion
1. Crea una cuenta en github.com. Si ya tienes una cuenta o creaste una mientras avanzabas en el capítulo Git y GitHub, puedes omitir este paso.
2. Crea un nuevo repositorio git con un archivo README.md y un archivo .gitignore (hay que elegir la plantilla de Python). Si necesitas repasar, consulta esta lección.
3. Si no lo has hecho, crea una cuenta en render.com. En esta lección se analizaron las aplicaciones web y de renderizado. Al crear una cuenta de Render, elige la opción "Github" y sigue los pasos de registro. Esto es exactamente lo que necesitas para vincular tu cuenta de Render a tu cuenta de GitHub.
4. Este proyecto implica realizar un análisis exploratorio de datos. Para lograrlo, necesitarás tener instalados los paquetes pandas y plotly-express. Anteriormente analizamos plotly en esta lección. plotly-express está diseñado con valores predeterminados razonables y opciones configurables para tipos de gráficos comunes, lo cual lo convierte en un excelente punto de partida para principiantes en comparación con solo plotly. Si eres principiante en esto, no te preocupes, ¡te guiaremos a través del proceso!

Además, necesitarás el paquete streamlit para desarrollar una aplicación web.

Crea un nuevo entorno virtual y asígnale un nombre significativo que esté relacionado con el conjunto de datos con el que trabajarás, por ejemplo, podrías llamarlo vehicles_env.

Asegúrate de haber instalado al menos los siguientes paquetes en el entorno: pandas, streamlit y plotly-express.

Si necesitas un resumen sobre cómo crear un entorno virtual e instalar paquetes, consulta la lección sobre este tema.

5. Instala VS Code si aún no lo has hecho. Clona el repositorio de tu proyecto desde GitHub y ábrelo como un proyecto en VS Code. Este será el directorio de tu proyecto. Configura el intérprete de Python como el utilizado por el entorno virtual que creaste anteriormente.
6. En aras de la simplicidad, en lugar de guardar tu entorno en el archivo requirements.txt del directorio del proyecto, crea manualmente el archivo requirement.txt y añade tres librerías ahí sin especificar las versiones:

 pandas
 plotly_express
 streamlit
 

## Paso 2. Descarga del archivo de datos
1. Descarga el conjunto de datos de anuncios de coches (vehicles_us.csv) o encuentra tu propio dataset en formato CSV.
2. Coloca el conjunto de datos en el directorio del proyecto.

## Paso 3. Análisis exploratiorio de datos
1. Crea un directorio llamado notebooks en el directorio de tu proyecto.
2. Crea un Jupyter notebook llamado EDA.ipynb en VS Code y guárdalo en el directorio notebooks de tu proyecto. Recuerda que .ipynb es una extensión de archivo para Jupyter Notebooks.
3. Abre el Jupyter notebook EDA.ipynb y experimenta con plotly-express para crear visualizaciones para el análisis exploratorio básico del conjunto de datos dentro del notebook. Estos son 

## Paso 4. Desarrollo del cuadro de mandos de la aplicación web
1. Crea un archivo app.py en la raíz del directorio de tu proyecto. Para crear un archivo .py, haz clic en "New File" (Nuevo archivo) en VS Code y guárdalo en el directorio del proyecto con el nombre deseado y la extensión .py.
2. Importa streamlit como st, pandas y plotly_express al principio del archivo.
3. Lee el archivo CSV del conjunto de datos en un DataFrame. El código será el mismo que tenías en el Jupyter Notebook al explorar el conjunto de datos.
4. Ahora, vamos a crear el contenido de nuestra aplicación basada en Streamlit. Esto es lo que queremos que incluyas:
- Al menos un encabezado (puedes utilizar st.header() para hacerlo. En la lección de aplicaciones web te mostramos cómo crear un encabezado).
- Crea un botón que, al hacer clic en él, construya un histograma plotly-express. Para hacerlo, considera utilizar las funciones st.write() y st.plotly_chart()

- Este es un ejemplo de cómo puedes hacerlo.

        import pandas as pd
        import plotly.express as px
        import streamlit as st
        
        car_data = pd.read_csv('vehicles_us.csv') # leer los datos
        hist_button = st.button('Construir histograma') # crear un botón
        
        if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

- Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión plotly-express. Nuevamente, considera utilizar las funciones st.write() y st.plotly_chart().
Esto es opcional, pero si quieres un desafío extra, considera reemplazar los botones por casillas de verificación, las cuales están disponibles en streamlit a través de st.checkbox(). Puedes pedirle al usuario o la usuaria que seleccione una casilla de verificación correspondiente a un histograma o un diagrama de dispersión y luego generar un gráfico basado en la casilla de verificación seleccionada. Este es un ejemplo simple de cómo funcionan las casillas de verificación en streamlit:

import streamlit as st

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
        ...
5. Asegúrate de actualizar el archivo README cuando hayas terminado. Este debe incluir una breve descripción del proyecto, donde se explique para qué sirve la aplicación web y qué tipo de funcionalidad proporciona.
6. Para hacer que Streamlit sea compatible con Render, añade un archivo de configuración de Streamlit al repositorio de tu proyecto en streamlit/config.toml con el siguiente contenido:
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
Le dirá a Render que busque en el sitio correcto para escuchar tu aplicación de Streamlit cuando la aloje en sus servidores.

7. Recuerda confirmar y empujar todos los cambios a tu repositorio cuando hayas terminado tu trabajo. Si no lo haces, nada funcionará correctamente.
Notas a considerar:

**Notas:**
Mientras desarrollas tu aplicación añadiendo un nuevo componente de Streamlit, puedes ejecutar el comando streamlit run app.py desde la terminal para ver el resultado.
Es una buena práctica confirmar y enviar tu trabajo a un repositorio remoto en GitHub a medida que vas alcanzando ciertos objetivos en el desarrollo de la aplicación (por ejemplo, añades un componente que funciona y la aplicación se ejecuta sin errores). ¡Así que no te olvides de escribir un mensaje de confirmación significativo!

## Paso 5. Despliegue de la version final de la aplicacion en Render

1. Accede a tu cuenta en render.com y crea un nuevo servicio web:

2. Crea un nuevo servicio web enlazado a tu repositorio de Github:

3. Configura el nuevo servicio web Render añadiendo un Build Command que instale todo lo necesario para iniciar tu app, incluyendo streamlit y todos los paquetes de requirements.txt. Utiliza el siguiente comando:
   pip install --upgrade pip && pip install -r requirements.txt
- Añade a tu Start Command: streamlit run app.py. Debería verse así:



4. Despliega en Render y espera a que el build se ejecute con éxito:


5. Comprueba que tu aplicación sea accesible a través de la siguiente URL: https://<APP_NAME>.onrender.com/.

**Notas:** pueden pasar varios minutos después de un despliegue exitoso hasta que la aplicación esté disponible online en un nivel gratuito. También hay que tener en cuenta que las aplicaciones se quedan "dormidas" después de estar inactivas durante unos minutos. Si es así, simplemente carga y actualiza tu aplicación unas cuantas veces para que se despierte.

Si actualizas tu repositorio de GitHub, para implementar la versión más reciente en Render, haz clic en "Manual Deploy" → "Latest Commit" (Implementación manual → Última confirmación).

¿Cómo puedo enviar mi proyecto?
Deberás enviar un enlace a tu repositorio de GitHub; también, añade la URL de tu aplicación en Render al README.md de tu proyecto.

¿Cómo será evaluado mi proyecto?
Hemos recopilado los criterios de evaluación del proyecto. Léelos detenidamente antes de enviarlo.

Esto es lo que buscan los revisores de proyecto cuando evalúan tu proyecto:

¿Contiene el repositorio del proyecto al menos los siguientes archivos?
$ tree
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
└── .streamlit
    └── config.toml

- ¿Se puede acceder a la aplicación web a través de un navegador?
- ¿Contiene la aplicación web los siguientes puntos?
  -Al menos un encabezado con texto.
  -Al menos un histograma.
  -Al menos un gráfico de dispersión.
  -Al menos un botón o una casilla de verificación.
