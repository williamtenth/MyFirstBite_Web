# -*- coding: utf-8 -*-
"""
Esta clase es un Singleton. Solo se generará una sola instancia de esta clase para la conexión a la base de datos.

Esta entidad contiene:

1. La información de conexión a la base de datos
2. El método de ejecución
"""
import configparser
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connector(object):

    __instance = None
    __nombre = None
    __database_host = None
    __database_port = None
    __database_name = None
    __database_user = None
    __database_pass = None
    __conexion = None
    __cursor = None
    __engine = None
    
    """ Método constructor con comportamiento Singleton. Sobrecarga __new__ """
    def __new__(cls):
        if Connector.__instance is None:
            Connector.__instance = object.__new__(cls)

        return Connector.__instance
    """ Método con la carga de variables de conexión por archivo .ini. Sobrecarga __init__"""
    def __init__(self):
        # Carga los datos de la conexión
        config = configparser.ConfigParser()
        config.read('../misc/config.ini')
        self.__database_host = config['DEFAULT']['DB_HOST']
        self.__database_port = config['DEFAULT']['DB_PORT']
        self.__database_name = config['DEFAULT']['DB_NAME']
        self.__database_user = config['DEFAULT']['DB_USER']
        self.__database_pass = config['DEFAULT']['DB_PASS']
        """ Conexión por SQLalchemy"""
        stringConnector = 'mysql://'+self.__database_user+':'+self.__database_pass+'@'+self.__database_host+'/'+self.__database_name
        __engine = create_engine(stringConnector)
    
    """ Métodos para conexión"""
    def __startConnection(self):
        self.__conexion = MySQLdb.connect( self.__database_host, self.__database_user, self.__database_pass, self.__database_name )
    
    def __closeConnection(self):
        self.__conexion.close()
    
    """     Método con la lógica básica     """
    def runQuery(self, query):
        self.__startConnection()
        self.__cursor = self.__conexion.cursor()
        self.__cursor.execute(query)
        for crm_info_id in self.__cursor.fetchall() :
            print (crm_info_id)
        self.__closeConnection()
    
    """ Métodos de Acceso"""
    def getEngine(self):
        return self.__engine
        
con = Connector()
print(con.getEngine)