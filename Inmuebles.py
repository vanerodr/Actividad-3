class Inmueble:
    def __init__(self, identificador, area, direccion):
        self._identificador = identificador
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"ID Inmobiliario: {self._identificador}")
        print(f"Área: {self._area} m²")
        print(f"Dirección: {self._direccion}")
        print(f"Precio de venta: ${self._precio_venta}")


class InmuebleVivienda(Inmueble):
    def __init__(self, identificador, area, direccion, habitaciones, banos):
        super().__init__(identificador, area, direccion)
        self._habitaciones = habitaciones
        self._banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self._habitaciones}")
        print(f"Baños: {self._banos}")


class Apartamento(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, habitaciones, banos):
        super().__init__(identificador, area, direccion, habitaciones, banos)


class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000

    def __init__(self, identificador, area, direccion, habitaciones, banos, valor_admon):
        super().__init__(identificador, area, direccion, habitaciones, banos)
        self._valor_admon = valor_admon

    def imprimir(self):
        super().imprimir()
        print(f"Administración: ${self._valor_admon}")
        print()


class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, identificador, area, direccion):
        super().__init__(identificador, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()


# Clase de prueba
if __name__ == "__main__":
    print("Datos apartamento familiar:")
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apto1.calcular_precio_venta(ApartamentoFamiliar.valor_area)
    apto1.imprimir()

    print("Datos apartaestudio:")
    apto2 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    apto2.calcular_precio_venta(Apartaestudio.valor_area)
    apto2.imprimir()
