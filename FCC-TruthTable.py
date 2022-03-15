
for i in range(0, 25):
    print("")

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

while True:
    x = input("\n\nIngresa tu expresión: ").upper()
    if x == "SALIR":
        break
    variables = []
    for i in x:
        print(i, end=' ')
        if i.isalpha() and not i in variables:
            variables.append(i)
    for i in range(2 ** len(variables)):
        print('')

        cadena = bin(i)[2:].rjust(len(variables), '0')
        booleano = list(map((lambda x: True if x == '1' else False), cadena))
        a = dict(zip(variables, booleano))
        calculo = []
        for j in x:
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
            else:
                print("Error: Vuelve a intentarlo")
              