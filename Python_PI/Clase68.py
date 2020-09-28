# Clase 68. Curso Píldoras Informáticas.

# Control de Flujo. Función Map. 

# - Es una función de orden superior. 
# - Forma parte del paradigma de la programación funcional. 
# - Aplica una función a cada elemento de una lista iterable y devuelve una lista con los resultados. 


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

# Tasa de letalidad de un goblin: 1.3 veces sus bajas confirmadas. 
def predictionkills(goblin):

	goblin.kills = round(goblin.kills * 1.3, 3)

	return goblin

listGoblinsPrediction = map(predictionkills, listGoblins)

for goblin in listGoblinsPrediction:

	print(goblin)
