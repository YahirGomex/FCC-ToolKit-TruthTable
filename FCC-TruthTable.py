#Se implementa un ciclo for para darle una mejor presentacion.
for i in range(0, 25):
    print("")

#Bienvenida
print(
    "-------------Bienvenido al generador de tablas de verdad-------------\n\n"
    "Explicación breve de la sintaxis:\n"
    "CONJUNCIÓN           -> &\n"
    "DISYUNCIÓN           -> |\n"
    "DISYUNCIÓN EXCLUSIVA -> ^\n"
    "NEGACIÓN             -> !\n"
    "IMPLICACIÓN          -> >\n"
    "DOBLE IMPLICACIÓN    -> <\n\n"
    "°Si deseas salir escribe 'SALIR'.\n"
    "°Te recomendamos abrir el PDF para aprovechar al máximo el programa.")

#Ciclo while para que siempre se mantenga dentro hasta que escriba la palabra clave
while True:
    #Solicitamos que ingrese la expresion y la convertimos a mayusculas para que todas las expresiones sean validas.
    x = input("\n\nIngresa tu expresión: ").upper()
    #Cabe la posibilidad de romper el ciclo.
    if x == "SALIR":
        break
    #Abrimos una lista para almacenar todos los datos necesarios.
    variables = []
    #Ciclo for dentro de la cadena 'x'
    for i in x:
        # Imprimimos el ciclo separado por espacio
        print(i, end=' ')
        #Colocamos un if para saber si lo que escribió el usuario es correcto y agregarlo a la lista 'variables'
        if i.isalpha() and not i in variables:
            variables.append(i)
            # Agregamos un ciclo for con el tamaño de variables elevado al cuadrado
    for i in range(2 ** len(variables)):
        print('')

        cadena = bin(i)[2:].rjust(len(variables), '0')
        # A partir de 'cadena', la variable 'booleano' arrojará si es verdadero o falso.
        booleano = list(map((lambda x: True if x == '1' else False), cadena))
        # la variable 'a' ocasiona que junte los valores de 'variables' y el resultado de 'booleanos'.
        a = dict(zip(variables, booleano))
        # Creamos la lista 'calculo' para realizar adjuntar todos los datos necesarios que se crearán dentro de las siguientes lineas de codigo
        calculo = []
        # Se crea el ciclo j dentro del ciclo i a partir de x.
        for j in x:
            # Ingresamos todos los condicionales.
            if j.isalpha():
                calculo.append(a[j])
                print(int(a[j]), end=' ')
            elif j == '&':
                calculo[-2] = calculo[-2] & calculo[-1]
                print(int(calculo[-2]), end=' ')
                del calculo[-1]
            elif j == '|':
                calculo[-2] = calculo[-2] | calculo[-1]
                print(int(calculo[-2]), end=' ')
                del calculo[-1]
            elif j == '^':
                calculo[-2] = calculo[-2] ^ calculo[-1]
                print(int(calculo[-2]), end=' ')
                del calculo[-1]
            elif j == '>':
                calculo[-2] = calculo[-2] <= calculo[-1]
                print(int(calculo[-2]), end=' ')
                del calculo[-1]
            elif j == '<':
                calculo[-2] = calculo[-2] >= calculo[-1]
                print(int(calculo[-2]), end=' ')
                del calculo[-1]
            elif j == '!' or j == '~':
                calculo[-1] = not calculo[-1]
                print(int(calculo[-1]), end=' ')
            # Le aclaramos que no es una expresion valida
            else:
                print("Error: Vuelve a intentarlo")

#Créditos para Benjamin Earl, el cual nos otorgó la orientación para el mapeado y acomodo de las variables.
              