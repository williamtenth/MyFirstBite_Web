from Connector import Connector

class ControllerAbs:
    __connector = None
    
    def __init__(self):
        __connector = Connector()
        
        __connector.runQuery( "SELECT crm_info_id FROM crm_information Limit 10" )
        
con = ControllerAbs()