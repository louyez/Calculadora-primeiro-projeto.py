#Comando para armazenar o histórico execultado:
historico = []

#Loop para reiniciar o programa futuramente:
while True:

        #É importante guardar o usuário, para registro do histórico dele depois:
        nome = str(input("Bem-vindo a sua calculadora programada. Para começarmos, me diga seu nome:"))

        #O usuário digita um número inteiro. Caso não seja verdadeiro, o laço se repete, obrigando o usuário a colaborar com o cálculo:
        while True:
                try:
                        n1 = int(input(f"Olá, {nome}! Digite agora o primeiro número para cálculo:"))
                        break
                except ValueError:
                        print("Digite apenas números inteiros")
                
        #O usuário escolhe um operador. Caso não seja verdadeiro, o laço se repete, obrigando o usuário a colaborar com o cálculo:
        while True:
                try:
                        operador = str(input("Certo. Preciso que escolha o operador correspondente ao cálculo desejado: \n" + 
                                              "[+] - Adição\n" + 
                                              "[-] - Subtração\n" +
                                              "[*] - Multiplicação\n" +
                                              "[/] - Divisão "))

                        if operador in ["+", "-", "*", "/"]:
                                break
                        else:
                                print("Digite um operador válido.")
                except ValueError:
                        print("Digite um operador válido.")

        #O usuário digita um número inteiro. Caso não seja verdadeiro, o laço se repete, obrigando o usuário a colaborar com o cálculo:
        while True:
                try:
                        n2 = int(input("Digite agora o segundo número e veja a magia acontecer:"))
                        break
                except ValueError:
                        print("Digite apenas números inteiros")
        
        #Se as definições anteriores estiverem corretas, o comando "if" é execultado:
        if operador == "+":
                resultado = n1 + n2
                print(f"O valor do cálculo de {nome} é:", n1 + n2)
        elif operador == "-":
                resultado = n1 - n2
                print(f"O valor do cálculo de {nome} é:", n1 - n2)
        if operador == "*":
                resultado = n1 * n2
                print(f"O valor do cálculo de {nome} é:", n1 * n2)
        elif operador == "/":
                resultado = n1 / n2
                print(f"O valor do cálculo de {nome} é:", n1 / n2)

        # Adiciona a operação ao histórico
        historico.append(f"{nome} {n1} {operador} {n2} = {resultado}")

#Etapa "2" do código:

        try:
                reiniciar = str(input("Fim do programa! Você pode reiniciá-lo digitando [R]\n"
                "Ou ver o histórico do usuário digitado [H]")).upper()

                if reiniciar == "R":
                       continue  # Reinicia o loop principal
                elif reiniciar == "H":
                        print("Histórico:")
                        for operacao in historico:
                                print(operacao)
                        break  # Sai do loop principal
                else:
                        print("Comando inválido. Saindo do programa.")
                        break  # Sai do loop principal

        except ValueError:
                print("Comando inválido")

                