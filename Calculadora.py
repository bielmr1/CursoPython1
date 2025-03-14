executar = True
while executar:
    escolhas = '''
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [/] para Dividir
        [4] ou [*] para Multiplicar
        [5] para sair.
        '''
    print(escolhas)
    operador = input("Qual sua opção?: ")
    n1 = (input("Qual é o primeiro número? "))
    n2 = (input("Qual é o segundo número? "))
    n1 = int(n1)
    n2 = int(n2)

    texto_sair = '''
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro cálculo!
    '''
    #Soma
    if operador == "1" or operador == "+" or operador == "Somar":
        resultado = n1 + n2
        print("Resultado da soma é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False
    #Subtração
    if operador == "2" or operador == "-" or operador == "Somar":
        resultado = n1 - n2
        print("Resultado da subtração é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False
    #Divisão
    if operador == "3" or operador == "/" or operador == "Dividir":
        resultado = n1 / n2
        print("Resultado da divisão é: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False
    #Multiplicação
    if operador == "4" or operador == "x" or operador == "Multiplicar":
        resultado = n1 * n2
        print("Resultado da multiplicação é: " +str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False
    #Sair
    if operador == "5" or operador == "Sair":
        print("Obrigado!")
        executar = False