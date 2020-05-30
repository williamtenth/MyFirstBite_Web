from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
stringConnector = 'mysql://root:admin1@localhost/sakila'
engine = create_engine(stringConnector)
Session = sessionmaker(bind=engine)
session = Session()

class Entity(Base):
    __tablename__ = 'entidad'
    id = Column(Integer, primary_key=True)
    
class Message(Base):
    __tablename__ = 'mensages'
    id = Column(Integer, primary_key=True)

entidad = Entity()
#Base.metadata.create_all(engine)
# session.add(entidad)
# session.commit()
query = session.query(Entity)
instance = query.first()
print(instance.id)
    
# metadata = MetaData()
# messages = Table('messages', metadata,
    # Column('id', Integer, primary_key=True),
    # Column('message', Text),
# )

# messages.create(bind=engine)