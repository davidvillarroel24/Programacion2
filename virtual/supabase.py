from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from sqlalchemy import create_engine
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
# https://docs.sqlalchemy.org/en/20/core/pooling.html#switching-pool-implementations
# engine = create_engine(DATABASE_URL, poolclass=NullPool)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")


class Base(DeclarativeBase):
    pass

class Empleado(Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    telefono=Column(Integer, nullable=False)

    #cargo = Column(String, nullable=False)
    #salario = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.id},{self.nombre}, {self.correo},{self.telefono}"# {self.cargo}, {self.salario}" 

#Base.metadata.create_all(engine)

def creaer_empleado(nombre,correo,telefono):
    #NuevoEmpleado=Empleado(nombre=nombre,cargo=cargo,salario=salario,email=correo)
    NuevoEmpleado=Empleado(nombre=nombre,correo=correo,telefono=telefono)
    with Session(engine) as session:
        session.add(NuevoEmpleado)
        session.commit()

def listar_empleados():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        result=session.query(Empleado).all()
        #result=session.get(Empleado,1)
        for empleado in result:
            print(empleado)

def eliminar_empleado(id_empleado):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        #result=session.query(Empleado).all()
        result=session.get(Empleado,id_empleado)
        if result:
            session.delete(result)
            session.commit()

def actualizar(id_empleado,nombre,correo,telefono):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        #result=session.query(Empleado).all()
        result=session.get(Empleado,id_empleado)
        if result:            
            result.nombre=nombre
            result.correo=correo
            result.telefono=telefono
            session.commit()
    pass

#eliminar_empleado(5)
#creaer_empleado("jesus","jesus@gmail.com",69517258)
listar_empleados()
#actualizar(6,"David","david@gmail.com",76923959)
#listar_empleados()