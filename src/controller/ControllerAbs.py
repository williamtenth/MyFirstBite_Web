from Connector import Connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ControllerAbs:
    __connector = Connector()
    session = None
       
    def __init__(self):
        self.__connector.runQuery( "SELECT crm_info_id FROM crm_information Limit 10" )
        Session = sessionmaker(bind=self.__connector.getEngine())
        self.session = Session()
        
con = ControllerAbs()
print(con.session)