from sqlalchemy import Column, String, Integer

class CRMInformationEntity(Base):
    __tablename__ = "crm_information"

    crm_info_id = Column(Integer, primary_key=True)
    tipo_documento = Column(String)
    num_documento = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    correo_electronico = Column(String)
    estado_postulacion = Column(String)
    causal_est_postulacion = Column(String)
    como_aclara = Colum(String)
    fecha_radicacion = Column(String)
    fecha_asignacion = Column(String)

