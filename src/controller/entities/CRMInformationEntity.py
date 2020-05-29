from sqlalchemy import Column, String, Integer

class CRMInformationEntity():
    __tablename__ = "crm_information"

    crm_info_id = Column(Integer, primary_key=True)
    tipo_documento = Column(String)
    num_documento = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    correo_electronico = Column(String)
    estado_postulacion = Column(String)
    causal_est_postulacion = Column(String)
    como_aclara = Column(String)
    fecha_radicacion = Column(String)
    fecha_asignacion = Column(String)
    
    def __repr__(self):
        return "<CRMInformationEntity(id='%s', tipo_doc='%s', num_doc='%s', nombres_apellido='%s')" % (self.crm_info_id, self.tipo_documento, self.num_documento, self.nombres + ' ' + self.apellidos)
