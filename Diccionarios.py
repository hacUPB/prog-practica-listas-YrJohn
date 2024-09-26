# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con elementos
mi_diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

nombre = mi_diccionario["nombre"]
edad = mi_diccionario["edad"]
mi_diccionario["profesión"] = "Ingeniera"
print(edad)
mi_diccionario["edad"] = 26
edad=mi_diccionario["edad"]
print(edad)
mi_diccionario["edad"] = 62
print(edad)
profesion=mi_diccionario["profesión"]
print (profesion)


conjuntoa=[]
conjuntob=[]
for i in range(1,6):
    conjuntoa.append(i)

    print(conjuntoa)

for i in range (4,9):
    conjuntob.append(i)