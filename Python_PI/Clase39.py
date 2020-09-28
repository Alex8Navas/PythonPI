# Clase 39. Curso Píldoras Informáticas.

# Control de Flujo. Serialización 1.

# Serializar es guardar en un archivo binario un objeto, colección...
# El objetivo es: 1. facilitar la distribución del archivo en internet, 
# 2. guardar el objeto en una base de datos. 

# La biblioteca de Python para esto es Pickle, que tiene los métodos:
# dump(): sirve para volcar datos al fichero binario externo. 
# load(): sirve para importar datos del fichero binario externo. 

import pickle 

Lista_Razas = ["Elfos", "Humanos", "Enanos", "Orcos"]

# wb es para codificar en binario el texto a crear (write binary).
Edad_Media = open("Tierra_Media", "wb") 

pickle.dump(Lista_Razas, Edad_Media)

Edad_Media.close()

# Una vez creado el fichero se puede eliminar de memoria el objeto que lo contiene.

del(Edad_Media)

# Leer e importar el fichero binario (rb: read binary)
ImportarTierraMedia = open("Tierra_Media", "rb")

Razas_Importadas = pickle.load(ImportarTierraMedia)

# Guarda el orden en que se exportaron. 
print(Razas_Importadas)

