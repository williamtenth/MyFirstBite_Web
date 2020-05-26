from Connector import Connector

class ControllerAbs:
    __connector = None
    
    def __init__(self):
        __connector = Connector()
        
        #__connector.startConnection()
        # __connector.cursor.execute( "SELECT crm_info_id FROM crm_information Limit 10" )
        # for crm_info_id in __connector.cursor.fetchall() :
            # print (crm_info_id)
            

# def ejecutarConsulta (cadena):
    # __connector.cursor.execute(cadena)
    

con = ControllerAbs()