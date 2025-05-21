class Persona:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion: str):
        self._direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def getCarrera(self):
        return self._carrera

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def getSemestre(self):
        return self._semestre

    def setSemestre(self, semestre: int):
        self._semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def getDepartamento(self):
        return self._departamento

    def setDepartamento(self, departamento: str):
        self._departamento = departamento

    def getCategoria(self):
        return self._categoria

    def setCategoria(self, categoria: str):
        self._categoria = categoria


# Prueba rápida
if __name__ == "__main__":
    estudiante = Estudiante("Ana", "Calle 123", "Ingeniería", 3)
    profesor = Profesor("Dr. Gómez", "Av. Central", "Matemáticas", "Titular")

    print("Estudiante:")
    print(f"Nombre: {estudiante.getNombre()}")
    print(f"Carrera: {estudiante.getCarrera()}")
    print(f"Semestre: {estudiante.getSemestre()}")

    print("\nProfesor:")
    print(f"Nombre: {profesor.getNombre()}")
    print(f"Departamento: {profesor.getDepartamento()}")
    print(f"Categoría: {profesor.getCategoria()}")
