lista=[2,3,4]
nombres=['JAZ', 'JOSS', 'JESS']

#En la poscion 0 inserta 1
lista.insert(0, 1) 
nombres.insert(0, 'JUSS')
nombres.insert(4, 'JUSS')
print(lista)
print(nombres)

#En la poscion 4 inserta 5
lista.insert(4, 5)
print(lista)


#Elimina el valor 3
lista.remove(3)
nombres.remove('JAZ')
print(lista)
print(nombres)

#Muestra el valor de la posicion 3
print(lista[2])

#Añade un elemento al final de la lista
lista.append(9)
print(lista)

#invierte el orden
lista.reverse()
print(lista)

#Ordena de menor a mayor
lista.sort()

#Muestra el tamaño de la lista
print(len(nombres))


#Cuenta el numero de vecs que aparece 
print(nombres.count('JUSS'))
