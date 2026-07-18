contador = 0
while True:
    comando = input("Digite 1 para clicar ou 0 para sair: ")

    if comando == "1":
        contador += 1
        print(f"Cliques: {contador}")

    elif comando == "0":
        break
    