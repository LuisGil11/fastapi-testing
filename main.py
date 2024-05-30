# Cree una aplicación sencilla en FastAPI que tenga dos endpoints: uno para obtener 
# todos los registros de una base de datos de usuarios (simulada en una lista) y otro 
# que solicite solo un registro por su id. Cree la pruebas unitarias que 
# prueben: la existencia de ambos endpoint, el correcto funcionamiento cuando se 
# soliciten todos los registros el correcto funcionamiento cuando se solicite uno 
# en particular, por su id y que detecte la falla cuando se le suministre un id 
# inválido (el id será el indice del usuario en la lista) A continuación cree el 
# arhivo Dockerfile que permita conteneirizar la aplicación y el archivo docker-compose.yml 
# para hacer el despliegue. No olvide que va a requerir un archivo de requirements.txt 
# para instalar las dependencias.

# Una vez finalizado comprima la carpeta en .zip o .rar y carguela 
# en el lugar indicado en esta pregunta

# Como base de datos use la siguiente lista: 
usuarios = [ ["Pedro Perez", 28, "pperez@prueba.com"], ["María Rosales", 26, "mrosales@prueba.com"], ["Juan Martinez", 32, "jmartinez@prueba.com"], ["Ana Gómez", 24, "agomez@prueba.com"], ["Carlos Ramirez", 30, "cramirez@prueba.com"], ["Lucia Fernández", 29, "lfernandez@prueba.com"], ["Jorge Herrera", 27, "jherrera@prueba.com"], ["Laura Torres", 25, "ltorres@prueba.com"], ["Roberto Diaz", 33, "rdiaz@prueba.com"], ["Silvia Sánchez", 31, "ssanchez@prueba.com"], ["Andrés Pérez", 26, "aperez@prueba.com"], ["Natalia Morales", 28, "nmorales@prueba.com"], ["Miguel Campos", 35, "mcampos@prueba.com"], ["Elena Ríos", 22, "erios@prueba.com"], ["Pablo Castro", 34, "pcastro@prueba.com"], ["Claudia León", 29, "cleon@prueba.com"], ["Felipe Vargas", 32, "fvargas@prueba.com"], ["Verónica Salazar", 27, "vsalazar@prueba.com"], ["Luis García", 30, "lgarcia@prueba.com"], ["Andrea Peña", 25, "apena@prueba.com"], ["Raúl Martínez", 28, "rmartinez@prueba.com"], ["Carmen Ruiz", 31, "cruiz@prueba.com"], ["Francisco Flores", 33, "fflores@prueba.com"], ["Isabel Ramos", 26, "iramos@prueba.com"], ["Victor Castillo", 29, "vcastillo@prueba.com"]]

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def read_root():
    return usuarios


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if (0 <= user_id < len(usuarios)):
        return usuarios[user_id]
    return f'user with id = {user_id} not found.'
