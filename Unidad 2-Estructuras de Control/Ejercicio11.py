<<<<<<< HEAD
#Autor: Deyberth Carrillo
#Entrada: Cantidad a retirar
#Salida: Saldo restante

#Se establece el saldo inicial
saldo=3000

#Se solicita la cantidad a retirar
print("Ingrese la cantidad a retirar")
retiro=int(input())

#Se evalua si la cantidad a retirar es valida y se efectua el retiro
if retiro>saldo:
    print("La cantidad ingresada para el retiro es mayor al saldo disponible\nSeleccione otra cantidad")
else:
    saldo-=retiro

#Se imprime la cantidad restante de saldo
print("El saldo restante es de: "+str(saldo))
=======
#Autor: Deyberth Carrillo
#Entrada: Cantidad a retirar
#Salida: Saldo restante

#Se establece el saldo inicial
saldo=3000

#Se solicita la cantidad a retirar
retiro=float(input())

#Se evalua si la cantidad a retirar es valida y se efectua el retiro
if retiro>saldo:
   print ("La cantidad maxima a sacar es 3000.00")
else:
    saldo-=retiro

#Se imprime la cantidad restante de saldo
print(saldo)
>>>>>>> b59401ad4195ebbde55d550f0d4ba0b9ab9a1219
