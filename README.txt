DESAFIO FINAL - BLOG TURISMO - CHACO TURISMO
Este blog lo creamos para el desafio final, se trata de un blog que implementa principalmente las funciones del CRUD. 
Pero tambien agregamos algunos contadores de interacciones, y estamos listos para agregarle muchas cosas mas!

Comenzando 🚀
Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones

Pre-requisitos 📋
Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:

virtualenv nombre-entorno

Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):

nombre_del_entorno\Scripts\activate.bat

Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto.

Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola.

pip install -r requirements.txt

Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente.

SETTINGS 🔧
Luego tenes que crear un archivo de configuraciones en la carpeta proyecto/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

Construido con 🛠️
Las herramientas utilizadas para el desarrollo fueron:

Django Framework web
Python Del lado del servidor (backend)
Bootstrap Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
MySql - Sistema de gestión de bases de datos.

Autor ✒️
Proyecto desarrollado por:

•Malena Gisel Rodriguez
•José Ángel Figueroa 
•Hector Daniel Mosqueira
•Fernando Javier Svoboda
•Antonella Ruelli



También puedes mirar la lista de todos los contribuyentes quíenes han participado en este proyecto.

