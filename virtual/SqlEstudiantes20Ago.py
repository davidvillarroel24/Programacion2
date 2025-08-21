from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy import  Date


#'allphylinux SO para que funcione como servidor de base de datos'

engine = create_engine('mysql+mysqlconnector://root@127.0.0.1:306/progra2')

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")

class Base(DeclarativeBase):
    pass

class Empleado(Base):
    __tablename__ = 'estudiantes'
    ci = Column(String(20), primary_key=True,autoincrement=False)
    nombre = Column(String(100), nullable=False)
    apellido1 = Column(String(100), nullable=False)
    apellido2 = Column(String(100), nullable=True)    
    genero = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(100), nullable=False)
    fechaNac = Column(Date, nullable=False)
    carrera = Column(String(100), nullable=False)
    nivel = Column(Integer, nullable=False)



    def __str__(self):
        return f"{self.ci},{self.nombre}, {self.apellido1}, {self.apellido2}, {self.genero}, {self.correo}, {self.telefono}, {self.fechaNac}, {self.carrera}, {self.nivel}" 

Base.metadata.create_all(engine)

def creaer_empleado(ci, nombre, apellido1, apellido2, genero, correo, telefono, fechaNac, carrera, nivel):
    NuevoEmpleado=Empleado(ci=ci, nombre=nombre, apellido1=apellido1, apellido2=apellido2, genero=genero, correo=correo, telefono=telefono, fechaNac=fechaNac, carrera=carrera, nivel=nivel)
    with Session(engine) as session:
        session.add(NuevoEmpleado)
        session.commit()

""" def creaer_empleado(nombre,cargo,salario,correo):
    NuevoEmpleado=Empleado(nombre=nombre,cargo=cargo,salario=salario,email=correo)
    with Session(engine) as session:
        session.add(NuevoEmpleado)
        session.commit() """

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

def actualizar(ci,nombre,apellido1,apellido2,genero,correo,telefono,fechaNac,carrera,nivel):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        #result=session.query(Empleado).all()
        result=session.get(Empleado,ci)
        if result:            
            result.nombre=nombre
            result.apellido1=apellido1
            result.apellido2=apellido2
            result.genero=genero
            result.correo=correo
            result.telefono=telefono
            result.fechaNac=fechaNac
            result.carrera=carrera
            result.nivel=nivel
            session.commit()

""" def actualizar(id_empleado,nombre,cargo,salario,correo):
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
            """
    

opcion=""
while True:
    print("1. Crear Estudinte")
    print("2. Listar Estudiantes")
    print("3. Eliminar Estudiante")
    print("4. Actualizar Estudiante")
    print("5. Salir")
    opcion=input("Ingrese una opcion: ")
    
    if opcion=="1":
        ci=input("Ingrese el CI del estudiante: ")
        nombre=input("Ingrese el nombre del estudiante: ")
        apellido1=input("Ingrese el primer apellido del estudiante: ")
        apellido2=input("Ingrese el segundo apellido del estudiante: ")
        genero=input("Ingrese el genero del estudiante: ")
        correo=input("Ingrese el correo del estudiante: ")
        telefono=input("Ingrese el telefono del estudiante: ")
        fechaNac=input("Ingrese la fecha de nacimiento del estudiante (YYYY-MM-DD): ")
        carrera=input("Ingrese la carrera del estudiante: ")
        nivel=int(input("Ingrese el nivel del estudiante: "))
        creaer_empleado(ci, nombre, apellido1, apellido2, genero, correo, telefono, fechaNac, carrera, nivel)
    elif opcion=="2":
        listar_empleados()
    elif opcion=="3":
        id_empleado=int(input("Ingrese el ID del empleado a eliminar: "))
        eliminar_empleado(id_empleado)
    elif opcion=="4":
        ci=input("Ingrese el CI del estudiante a actualizar: ")
        nombre=input("Ingrese el nuevo nombre del estudiante: ")
        apellido1=input("Ingrese el nuevo primer apellido del estudiante: ")
        apellido2=input("Ingrese el nuevo segundo apellido del estudiante: ")
        genero=input("Ingrese el nuevo genero del estudiante: ")
        correo=input("Ingrese el nuevo correo del estudiante: ")
        telefono=input("Ingrese el nuevo telefono del estudiante: ")
        fechaNac=input("Ingrese la nueva fecha de nacimiento del estudiante (YYYY-MM-DD): ")
        carrera=input("Ingrese la nueva carrera del estudiante: ")
        nivel=int(input("Ingrese el nuevo nivel del estudiante: "))
        actualizar(ci, nombre, apellido1, apellido2, genero, correo, telefono, fechaNac, carrera, nivel)
    elif opcion=="5":
        break
    else:
        print("Opcion no valida, intente de nuevo.")
 
#eliminar_empleado(13)
#creaer_empleado("jesus","programador",2000,"jesus@gmail.com")
#listar_empleados()
#actualizar(13,"luis","programador",2500,"luis17@gmail.com")
#listar_empleados()
