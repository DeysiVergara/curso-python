#Definicion de una funcion

#def nombre_de_la_funcion(params):
    #docstring
    #cuerpo de la funcion
    # return valor_retorno #opcional


# def saludar(nombre):
#     print(f"Hola {nombre}!")

# saludar("cariñito")
# saludar("bombon")
# saludar("preciosa")

# def sumar(a,b):
#     suma = a + b
#     return suma

# result = sumar(2,8)
# print(result)

# #documentar con docstring
# def restar(a,b):
#     """Resta dos numeros y devuelve el resultador"""
#     return a-b

# result = restar(10,8)
# print(result)

# help(restar)

# def multiplicar(a, b = 2):
#     return a*b

# print(multiplicar(2))
# print(multiplicar(2,6))

#Argumento por clave
# def describir_persona(nombre, edad, sexo):
#     print(f"Soy {nombre}, tengo {edad} y me identifico como {sexo}")

# describir_persona("deysi", 33, "mujer")
# describir_persona(sexo="gato", nombre="Lelish", edad= 45)

# def sumar_numeros(*args):
#     suma = 0
#     for numero in args:
#         suma += numero
#     return suma
# print(sumar_numeros( 8, 4, 5))

def mostrar_info_de(**kwargs):
    for clave, valor in kwargs.items():
          print(f"{clave}: {valor}")

mostrar_info_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_info_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_info_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_info_de(super_name="felixicaza", es_modo=True, gatos=40)
