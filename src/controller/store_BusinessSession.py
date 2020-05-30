from BusinessSessionAbs import BusinessSessionAbs
from entities.store_Entity import store_Entity

class store_BusinessSession(BusinessSessionAbs):
    
    def getStoreByID(self,crm_info_id):
        print('Funcion: getCRMByID()')
        print(self.session)
        # print(self.session)
        
        store = self.session.query(store_Entity).first()
        print(store)

crm = store_BusinessSession()
crm.getStoreByID(1)