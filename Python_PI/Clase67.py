# Clase 67. Curso Píldoras Informáticas.

# Control de Flujo. Función Filter. 

# - Es una función de orden superior. 
# - Forma parte del paradigma de la programación funcional. 
# - Verifica que los elementos de una secuencia cumplen una condición y devuelve un iterador de los elementos que la cumplen. 

def par(number):

	if number % 2 == 0:

		return True

numberlist = [3,4,5,6,7,8,9,10]

print(list(filter(par, numberlist))) # Si no se pone list devuelve un objeto con filter, pero no la lista en sí. 

# Con función lambda acoplada:
print(list(filter(lambda par: par % 2 == 0, numberlist)))

# Casi siempre se usa filter para filtrar objetos, no listas:
class Goblin:

	def __init__(self, name, village, kills):

		self.name = name

		self.village = village

		self.kills = kills

	def __str__(self):

		return """	Un goblin ha llegado a la aldea de {}.
Su nombre es {}. Es un héroe de guerra con más de
{} bajas confirmadas en combate.
		""".format(self.village, self.name, self.kills)

listGoblins = [

Goblin("Johannes", "Krotea", 6),
Goblin("Draknar", "Krotea", 65),
Goblin("Terl", "Krotea", 12),
Goblin("Bárgana", "Krotea", 2),
Goblin("Quixane", "Krotea", 4),
Goblin("Gojn", "Krotea", 14),
Goblin("Pérgamo", "Krotea", 8),
Goblin("Frexar", "Krotea", 11)

]

# Se aplica la función filter al objeto creado.  

herosList = filter(lambda goblin: goblin.kills > 10, listGoblins)

# Se recorre el objeto devuelto por filter:

for goblin in herosList:

	print(goblin)

notRealHeros = filter(lambda goblin: goblin.kills < 10, listGoblins)

for goblin in notRealHeros:

	print(goblin)



