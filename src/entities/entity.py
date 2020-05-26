# -*- coding: utf-8 -*-
"""
Esta entidad contiene:
1. La información de conexión a la base de datos
2. El objeto con la conexión a la base de dato
"""
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine =
#Se obtiene la configuración de conexión 
config = configparser.ConfigParser()
config.read('..\config.ini')

database_name = config['DEFAULT']['DB_NAME']
database_pass = config['DEFAULT']['DB_PASSWORD']
database_user = config['DEFAULT']['DB_USER']

print(database_name, " hola")
print(database_pass)
print(database_user)

#