# Clase 6. Curso Píldoras Informáticas.

# Función Suma: 
def suma():
	number1 = 5
	number2 =9
	print(number1 + number2)

suma()

# Función Suma con parámetros: 
def sumapam(number1, number2):
	print(number1 + number2)

sumapam(8 , 9)
sumapam(7 , 4)
sumapam(3 , 8)
sumapam(number2 = 3, number1 = 4)


def sumapam_return(number1, number2):
	resultado = number1 + number2
	return resultado

print(sumapam_return(4, 5))

Valor_Suma = sumapam_return(8, 5)
print(Valor_Suma)

