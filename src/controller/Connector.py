# -*- coding: utf-8 -*-
"""
Esta clase es un Singleton. Solo se generará una sola instancia de esta clase para la conexión a la base de datos.

Esta entidad contiene:

1. La información de conexión a la base de datos
2. El objeto con la conexión a la base de dato
"""
import configparser
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connector(object):

    __instance = None
    nombre = None
    database_host = None
    database_port = None
    database_name = None
    database_user = None
    database_pass = None
    conexion = None
    cursor = None
    
    def __str__(self):
        return self.__repr__() + ' ' + self.nombre
        
    def __connection_test__(conn):
        cur = conn.cursor()
        #cur.execute( "SELECT crm_info_id FROM crm_information limit 10" )
        #for crm_info_id in cur.fetchall() :
            #print (crm_info_id)

    def __new__(cls):
        if Connector.__instance is None:
            Connector.__instance = object.__new__(cls)
            # Carga los datos de la conexión
            config = configparser.ConfigParser()
            config.read('../controller/config.ini')
            database_host = config['DEFAULT']['DB_HOST']
            database_port = config['DEFAULT']['DB_PORT']
            database_name = config['DEFAULT']['DB_NAME']
            database_user = config['DEFAULT']['DB_USER']
            database_pass = config['DEFAULT']['DB_PASS']
            print(database_host)
            
            # Genera la conexión a la db
            # conexion = MySQLdb.connect(database_host, database_user, database_pass, database_name)
            # cursor = conexion.cursor()
            # cursor.execute( "SELECT crm_info_id FROM crm_information Limit 10" )
            # for crm_info_id in cursor.fetchall() :
                # print (crm_info_id)
            
        return Connector.__instance

    def startConnection(self):
        print('hola')
        print(database_host)
        #conexion = MySQLdb.connect(database_host, database_user, database_pass, database_name)
        #cursor = conexion.cursor()
        
    # def closeConnection(self):
        # conexion.close()
    
    

#test1 = Connector()
# test1.nombre = "test1"
# print(test1)
# test2 = Connector()
# test2.nombre = "test2"
# print(test2)

# print(test1)
# print(test2)