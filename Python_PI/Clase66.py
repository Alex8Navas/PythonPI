# Clase 66. Curso Píldoras Informáticas.

# Control de Flujo. Funciones Lambda. 

# - Son típicas de los lenguajes Lisp y JavaScript.
# - Son funciones anónimas que sirven para aliviar, para simplificar el código. 
# Otros nombres: funciones on the go, funciones on demand, funciones online. 

# Función normal:
def areaTriangulo(base, altura):

	return (base*altura)/2

print(areaTriangulo(5,6))

# Función Lambda para área de triángulo:
areaTrianguloL = lambda base, altura: base*altura/2
print(areaTrianguloL(4,4))

# Función lambda para elevr al cubo
elevaCubo = lambda number:pow(number, 3) 
print(elevaCubo(5))

# Función lambda para mostrar signos junto a números. 
dolarShow = lambda number: "Ha ganado usted {} $".format(number)
print(dolarShow(1500))

