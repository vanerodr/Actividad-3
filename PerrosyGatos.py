class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")


# ---------------- PERROS ---------------- #
class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Peso: {self.peso} kg")
        print(f"Muerde: {'Sí' if self.muerde else 'No'}")


class PerroPequeno(Perro): pass
class Caniche(PerroPequeno): pass
class YorkshireTerrier(PerroPequeno): pass
class Schnauzer(PerroPequeno): pass
class Chihuahua(PerroPequeno): pass

class PerroMediano(Perro): pass
class Collie(PerroMediano): pass
class Dalmata(PerroMediano): pass
class Bulldog(PerroMediano): pass
class Galgo(PerroMediano): pass
class Sabueso(PerroMediano): pass

class PerroGrande(Perro): pass
class PastorAleman(PerroGrande): pass
class Doberman(PerroGrande): pass
class Rottweiler(PerroGrande): pass


# ---------------- GATOS ---------------- #
class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Salto (altura): {self.altura_salto} cm")
        print(f"Salto (longitud): {self.longitud_salto} cm")


class GatoSinPelo(Gato): pass
class Esfinge(GatoSinPelo): pass
class Elfo(GatoSinPelo): pass
class Donskoy(GatoSinPelo): pass

class GatoPeloLargo(Gato): pass
class Angora(GatoPeloLargo): pass
class Himalayo(GatoPeloLargo): pass
class Balines(GatoPeloLargo): pass
class Somali(GatoPeloLargo): pass

class GatoPeloCorto(Gato): pass
class AzulRuso(GatoPeloCorto): pass
class Britanico(GatoPeloCorto): pass
class Manx(GatoPeloCorto): pass
class DevonRex(GatoPeloCorto): pass


# ---------------- PRUEBA ---------------- #
if __name__ == "__main__":
    rex = PastorAleman("Rex", 4, "negro y café", 32, True)
    luna = Angora("Luna", 2, "blanco", 85, 150)

    print("Información del perro:")
    rex.mostrar_info()
    rex.sonido()

    print("\nInformación del gato:")
    luna.mostrar_info()
    luna.sonido()
