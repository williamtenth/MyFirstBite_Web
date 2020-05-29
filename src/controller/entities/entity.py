# -*- coding: utf-8 -*-
"""
Esta entidad contiene:
1. La información de conexión a la base de datos
2. El objeto con la conexión a la base de dato
"""
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

