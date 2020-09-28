# Clase 32. Curso Píldoras Informáticas.

# Control de Flujo. POO9.

# Polimorfismo

class Car():

	def desplaza(self):

		print("El coche se desplaza sobre sus cuatro ruedas.")


class Moto():

	def desplaza(self):

		print("La moto se desplaza sobre sus dos ruedas.")


class Furgo():

	def desplaza(self):

		print("La furgo se desplaza sobre sus seis ruedas.")


print("----Sin Polimorismo----")

VehiculoUno = Moto()

VehiculoUno.desplaza()

VehiculoDos = Furgo()

VehiculoDos.desplaza()

VehiculoTres = Car()

VehiculoTres.desplaza()


print("----Con Polimorismo----")


def desplazaPolif(k):

	k.desplaza()

VehiculoCuatro = Furgo()

desplazaPolif(VehiculoCuatro)

VehiculoCinco = Moto()

desplazaPolif(VehiculoCinco)
