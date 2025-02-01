# print ("Bucle While:")
# contador = 0
# while contador <=5:
#     print(contador)
#     contador += 1 


# contador = 0

# while True:
#     print(contador)
#     contador += 1
#     if contador % 5 == 0 :
#         print("El número es multiplo de 5")
#         break  

# print("Bucle continuar")
# contador = 0
# while contador < 10 :
#     contador += 1
#     if contador % 2 == 0 :
#         continue
#     print(contador)

#else
# print("Bucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     # break
# else:
#     print("el bucle ha terminado")

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("El numero debe ser positivo, cariño")
    except:
        print("Debe ser un numero, cariño")
print(f"El numero introducido es {numero}")
