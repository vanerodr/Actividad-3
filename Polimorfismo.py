class Profesor:
    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")


# Prueba de polimorfismo
if __name__ == "__main__":
    profesor1 = ProfesorTitular()  # Referencia del tipo padre, instancia del tipo hijo
    profesor1.imprimir()  # Se ejecuta el método de ProfesorTitular
