from BusinessSessionAbs import BusinessSessionAbs
from entities.CRMInformationEntity import CRMInformationEntity

class CRM_BusinessSession(BusinessSessionAbs):

    def getByID(self,crm_info_id):
        print('Funcion: getCRMByID()')
        print(self.session)
        # print(self.session)

        CRMInfoData = self.session.query(CRMInformationEntity).first()
        #print (CRMInfoData)

    #def newRegister(Entity):


crm = CRM_BusinessSession()
crm.getByID(1)
