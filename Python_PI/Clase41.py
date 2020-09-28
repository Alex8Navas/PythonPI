# Clase 41. Curso Píldoras Informáticas.

# Control de Flujo. Guardado Permanente.

import pickle 

class Vampiro():

	def __init__(self, name, genre, age):

		self.name = name
		self.genre = genre
		self.age = age
		print("Ha nacido un vampiro sangre nueva.")

	def __str__(self):

		return "El presente vampiro se llama {}.\nSu género es {}.\nY su edad es de {} años".format(self.name, self.genre, self.age)


class ListaVampiro():

	SangreNueva = []

	def __init__(self): # Constructor para guardar la información de modo permanente. 

		ListadeVampiros = open("VampireText", "ab+") # ab+ significa agregar información binaria.
		ListadeVampiros.seek(0) # Se pone el cursor al comienzo del texto. 
		
		try: # Si el fichero está vacío la instrucción load dará error. 
		
			self.SangreNueva = pickle.load(ListadeVampiros) # Se cargan en el archivo los vampiros. 
			print("Se han creado {} sangre nueva".format(len(self.SangreNueva))) 
		
		except:

			print("El fichero se encuentra vacío.")

		finally:

			ListadeVampiros.close()
			del(ListadeVampiros)

	def AgregaVampiro(self, NewVamp):

		self.SangreNueva.append(NewVamp)
		self.GuardaVampiro() # Sirve para llamar al método de guardado creado. 

	def ShowVampiro(self):

		for i in self.SangreNueva:

			print(i) 

	def GuardaVampiro(self): # Guarda los vampiros en el fichero externo. 

		ListadeVampiros = open("VampireText", "wb")
		pickle.dump(self.SangreNueva, ListadeVampiros)
		ListadeVampiros.close()
		del(ListadeVampiros)

	def LeerVampireText(self): # Método para leer el fichero externo. 

		print("La información de las Crónicas Vampiras es:\n")
		for i in self.SangreNueva:
			print(i)


ListaVampire1 = ListaVampiro()


Vamp1 = Vampiro("Van Hess", "varón", 729)
Vamp2 = Vampiro("Van Roth", "varón", 527)
Vamp3 = Vampiro("Drexler", "varón", 651)
Vamp4 = Vampiro("Calstein", "hembra", 320)
Vamp5 = Vampiro("Niskova", "hembra", 870)

ListaVampire1.AgregaVampiro(Vamp1)
ListaVampire1.AgregaVampiro(Vamp2)
ListaVampire1.AgregaVampiro(Vamp3)
ListaVampire1.AgregaVampiro(Vamp4)
ListaVampire1.AgregaVampiro(Vamp5)
ListaVampire1.ShowVampiro()
ListaVampire1.LeerVampireText()

