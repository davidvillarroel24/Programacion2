from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


engine = create_engine('mysql+mysqlconnector://root@127.0.0.1:306/progra2')

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
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    cargo = Column(String(100), nullable=False)
    salario = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.id},{self.nombre}, {self.email}, {self.cargo}, {self.salario}" 

Base.metadata.create_all(engine)

def creaer_empleado(nombre,cargo,salario,correo):
    NuevoEmpleado=Empleado(nombre=nombre,cargo=cargo,salario=salario,email=correo)
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

def actualizar(id_empleado,nombre,cargo,salario,correo):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        #result=session.query(Empleado).all()
        result=session.get(Empleado,id_empleado)
        if result:            
            result.nombre=nombre
            result.cargo=cargo
            result.salario=salario
            result.correo=correo
            session.commit()
    pass

opcion=""
while True:
    print("1. Crear Empleado")
    print("2. Listar Empleados")
    print("3. Eliminar Empleado")
    print("4. Actualizar Empleado")
    print("5. Salir")
    opcion=input("Ingrese una opcion: ")
    
    if opcion=="1":
        nombre=input("Ingrese el nombre del empleado: ")
        cargo=input("Ingrese el cargo del empleado: ")
        salario=int(input("Ingrese el salario del empleado: "))
        correo=input("Ingrese el correo del empleado: ")
        creaer_empleado(nombre,cargo,salario,correo)
    elif opcion=="2":
        listar_empleados()
    elif opcion=="3":
        id_empleado=int(input("Ingrese el ID del empleado a eliminar: "))
        eliminar_empleado(id_empleado)
    elif opcion=="4":
        id_empleado=int(input("Ingrese el ID del empleado a actualizar: "))
        nombre=input("Ingrese el nuevo nombre del empleado: ")
        cargo=input("Ingrese el nuevo cargo del empleado: ")
        salario=int(input("Ingrese el nuevo salario del empleado: "))
        correo=input("Ingrese el nuevo correo del empleado: ")
        actualizar(id_empleado,nombre,cargo,salario,correo)
    elif opcion=="5":
        break
    else:
        print("Opcion no valida, intente de nuevo.")

#eliminar_empleado(13)
#creaer_empleado("jesus","programador",2000,"jesus@gmail.com")
#listar_empleados()
#actualizar(13,"luis","programador",2500,"luis17@gmail.com")
#listar_empleados()
