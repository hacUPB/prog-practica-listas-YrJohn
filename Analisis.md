#Analisis: 
Lo que haria: Primero, haria una lista que contenga el abecedario, luego de esto, cuando me den el texto a cifrar, usaria el abecedario antes planteado para buscar cada letra y cifrarla usando los subindices de la misma lista, creo que el unico problema seria cuando tenga que por asi decirlo, dar la vuelta para volver a repetir la lista, pero creo que se podria solucionar utilizando un bucle o algo similar, otra opcion seria repetir el abecedario dos veces para asi intentar solventar este problema a corto plazo, porque si dan un valor muy alto a cifrar acabaria en el mismo problema.

Correcion problema: Primero, recibiria el texto a cifrar y su indice de cifrado, luego usaria la tabla ascii para convertir las letras a numeros y asi poder convertirlos facilmente.
La operacion a realizar cuando el numero se pase, seria numero-122+97, para optimizarlo seria = numero-25





nueva=""
desplazamiento=
texto=
Pseudocodigo:
Inicio 
Leer texto
Leer indicecifrado
for letra in texto:
    numeroletra=ord(letra):
    si numeroletra >=97 and numeroletra<=122
    numeroletra +=desplazamiento
        si 122<numeroletra
            numeroletra-=25
            fin si
nueva+=chr(numero letra)








