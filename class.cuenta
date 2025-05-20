class Cuenta:
  def __init__(self, saldo, tasa_anual):
      self.saldo = saldo
      self.numero_consignaciones = 0
      self.numero_retiros = 0
      self.tasa_anual = tasa_anual
      self.comision_mensual = 0

  def consignar(self, cantidad):
      self.saldo += cantidad
      self.numero_consignaciones += 1

  def retirar(self, cantidad):
      if cantidad <= self.saldo:
          self.saldo -= cantidad
          self.numero_retiros += 1
      else:
          print("La cantidad a retirar excede el saldo actual.")

  def calcular_interes(self):
      tasa_mensual = self.tasa_anual / 12
      interes_mensual = self.saldo * tasa_mensual
      self.saldo += interes_mensual

  def extracto_mensual(self):
      self.saldo -= self.comision_mensual
      self.calcular_interes()


class CuentaAhorros(Cuenta):
  def __init__(self, saldo, tasa_anual):
      super().__init__(saldo, tasa_anual)
      self.activa = self.saldo >= 10000

  def consignar(self, cantidad):
      if self.activa:
          super().consignar(cantidad)

  def retirar(self, cantidad):
      if self.activa:
          super().retirar(cantidad)

  def extracto_mensual(self):
      if self.numero_retiros > 4:
          self.comision_mensual += (self.numero_retiros - 4) * 1000
      super().extracto_mensual()
      self.activa = self.saldo >= 10000

  def imprimir(self):
      print(f"Saldo = ${self.saldo}")
      print(f"Comisión mensual = ${self.comision_mensual}")
      print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
      print()


class CuentaCorriente(Cuenta):
  def __init__(self, saldo, tasa_anual):
      super().__init__(saldo, tasa_anual)
      self.sobregiro = 0

  def retirar(self, cantidad):
      if cantidad <= self.saldo:
          super().retirar(cantidad)
      else:
          diferencia = cantidad - self.saldo
          self.sobregiro += diferencia
          self.saldo = 0
          self.numero_retiros += 1

  def consignar(self, cantidad):
      if self.sobregiro > 0:
          if cantidad >= self.sobregiro:
              cantidad -= self.sobregiro
              self.sobregiro = 0
              self.saldo += cantidad
          else:
              self.sobregiro -= cantidad
      else:
          super().consignar(cantidad)

  def extracto_mensual(self):
      super().extracto_mensual()

  def imprimir(self):
      print(f"Saldo = ${self.saldo}")
      print(f"Comisión mensual = ${self.comision_mensual}")
      print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
      print(f"Sobregiro = ${self.sobregiro}")
      print()


# Prueba de Cuenta de Ahorros
if __name__ == "__main__":
  print("Cuenta de ahorros")
  saldo_inicial = float(input("Ingrese saldo inicial: $"))
  tasa_interes = float(input("Ingrese tasa de interés (ej. 0.05 para 5%): "))

  cuenta = CuentaAhorros(saldo_inicial, tasa_interes)

  deposito = float(input("Cantidad a consignar: $"))
  cuenta.consignar(deposito)

  retiro = float(input("Cantidad a retirar: $"))
  cuenta.retirar(retiro)

  cuenta.extracto_mensual()
  cuenta.imprimir()
