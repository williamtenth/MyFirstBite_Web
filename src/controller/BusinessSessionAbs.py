from Connector import Connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BusinessSessionAbs:
    __connector = Connector()

    def __init__(self):
        print("BusinessSessionAbs.__init__")
        #self.__connector.runQuery( "SELECT crm_info_id FROM crm_information Limit 10" )
        Session = sessionmaker(bind=self.__connector.getEngine())
        self.session = Session()

con = BusinessSessionAbs()

print('-------BusinessSessionAbs: Session ',con.session)
