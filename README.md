# curso Python Instagram2.0
Un curso mejor desarrollado para python e instagram, en donde explico como usar el api de instagram combinado con el scraping a los endpoints de esta platafroma.

Como usarlo ?
Descarga el proyecto de github

git clone https://github.com/ITBearYoutube/cursoPythonInstagram2.0.git

entra en la carpeta 

cd cursoPythonInstagram2.0

Para este proyecto usamos python 3.6

correr el sgt comando en python cuando se tenga activo el ambiente de python 3.6

pip install -r requeriments.tx

El credentials es donde debes poner tus credenciales de Instagram

Ejecutar el file bot.py para iniciar el programa

Si lo deseas ejecutar en una maquina en linux, primero da los permisos al file bot.py

sudo chmod 777 bot.py

En tu version de linux deberas buscar la ruta en donde se instalo el python 3.6
Puede ser algo parecido a esto: /home/ubuntu/anaconda3/envs/py366/bin/python

Una vez encontrada la ruta , editar el file bash.sh, en la variable RUTADEPYTHON
Guardar el .sh y ejecutar en la consola de linux:
crontab -e

Ingresar en la ventana el comando:
#10 08 * * * /home/ubuntu/cursoPythonInstagram2.0/bash.sh

Teclear  Ctrl + X y despues yes

El anterior comando lo hara ejecutar el script todos los dias a las 8:10 am


Y listo, si te gusto el tutorial en youtube, deja tu like y suscribete para mas cursos asi!!!

