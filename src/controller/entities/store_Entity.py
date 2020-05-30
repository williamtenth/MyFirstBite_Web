from sqlalchemy import Column, String, Integer

class store_Entity():
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True)
    manager_staff_id = Column(String)
    # num_documento = Column(String)
    # nombres = Column(String)
    # apellidos = Column(String)
    # correo_electronico = Column(String)
    # estado_postulacion = Column(String)
    # causal_est_postulacion = Column(String)
    # como_aclara = Column(String)
    # fecha_radicacion = Column(String)
    # fecha_asignacion = Column(String)
    
    # def __repr__(self):
        # return "<CRMInformationEntity(id='%s', tipo_doc='%s', num_doc='%s', nombres_apellido='%s')" % (self.crm_info_id, self.tipo_documento, self.num_documento, self.nombres + ' ' + self.apellidos)
