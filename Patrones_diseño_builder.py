"""
Patrones de diseño - Builder
en Python
"""
class Student:
    """
        La interfaz Builder especifica métodos para crear las diferentes partes de
        los objetos Producto, agregar mas funciones sin afectar la estructura.
        """
    def __init__(self, nstudiante):
        self.nstudiante = nstudiante

    def datos_estudiante(self):

        print(f"¡Bienevenido  {self.nstudiante} a la universidad del futuro ")

    def agregar_estudiante(self):
        print("*************************************")
        global c,n
        c=int(input("Ingrese Numero de Documento : "))
        n=str(input("Ingrese Nombre y Apellido : "))

        print("*************************************")

    def agregar_materias(self):
        print("*************************************")
        global m1,f1,dc1,semestre

        m1=str(input("""Selecione Materia:
            *. Programacion
            *. Matematicas
            *. Software                            """))
        f1=str(input("""Selecione Facultad:
            *. Sistemas
            *. Derecho
            *. Medicina                           """))
        dc1=str(input("""Selecione Docente :
            *. Carlos (Programacion)
            *. Pedro  (Matematicas)
            *. Paola  (Software)          """))
        semestre=str(input("""Selecione Semestre :
            1. I      4. IV       7. VII
            2. II     5. V
            3. III    6. VI             """))
        print("*************************************")


    def reporte(self):
        print(">>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<")
        print ("Estudiante : ",n,"Documento No ",c)
        print ("Materia : ",m1)
        print ("Facultad :",f1)
        print ("Docente : ",dc1)
        print ("Semestre :",semestre)
        print(">>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<")

Student = Student("Estudiante")
Student.datos_estudiante()
Student.agregar_estudiante()
Student.agregar_materias()
Student.reporte()
