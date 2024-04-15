import random

pokedex = []
print(f"\nOlá, eu sou o professor Carvalho, um pesquisador Pokémon.\nAnters de começarmos nossa jornada, qual é o seu nome?")
nome = str(input("\n-> "))
print(f"\nÓtimo, então você é o {nome}! Prepare-se para embarcar em uma aventura emocionante no mundo dos Pokémons!")
tentativa_captura = 3
captura = 0

#Looping "o que deseja fazer?" e suas escolhas
while True:
    if tentativa_captura == 0:
        print("\nAcabaram as tentativas... Reinicie o jogo\n")
        break
    escolha = int(input(f"\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Ver Pokédex\n4. Sair\n\n-> "))

    #Condição para evitar bug de escolha (fora do intervalo 1-4)
    if escolha < 1 or escolha> 4:
        print("\nEscolha uma opção válida!")
        continue

    #ENTRAR NA CAVERNA
    if escolha == 1:
            ja_tem_este_pokemon = 0
            print("\n\nEscolheu entrar na caverna")
            #POKEMONS CAVERNA
            pokemons_caverna = ["Pikachu", "Golem", "Blastoide"]
            pokemon_encontrado = None

            #Looping para decidir qual pokemon vai encontrar
            while True:
                pokemon_caverna = random.randint(0,10)
                if 0 <= pokemon_caverna <= 6: #60% de chance de capturar o Pikachu
                        pokemon_encontrado = pokemons_caverna[0]
                        break
                elif 7<=pokemon_caverna<=9: #30% de chance de capturar o Golem 
                        pokemon_encontrado = pokemons_caverna[1]
                        break
                elif pokemon_caverna == 10: #10% de chance de capturar o Blastoide
                        pokemon_encontrado = pokemons_caverna[2]
                        break
            print(f"\n-Você encontrou o {pokemon_encontrado}!-")
            if pokemon_encontrado in pokedex: #se o pokemon não estiver na pokedex, adicionar, se não, não adicionar
                print("\nVocê já tem este pókemon!\n")
                continue
            
            #Looping para tentar capturar o pókemon
            while True:
                escolha_caverna = int(input(f"\nDeseja tentar capturar {pokemon_encontrado}?\n1- Sim\n2- Não\n\n-> "))
                #TENTAR CAPTURAR
                if escolha_caverna == 1: 
                    chance_captura = random.randint(1,100)
                    if 1<=chance_captura<= 35:
                        print(f"\nPókemon {pokemon_encontrado} capturado com sucesso!\n")
                        pokedex.append(pokemon_encontrado)
                        captura += 1
                        break
                    elif 35<chance_captura<=100:
                        print(f"\nPókemon {pokemon_encontrado} não capturado, tente novamente!")
                        tentativa_captura -= 1
                        print(f"\nTentativas restantes: {tentativa_captura}")
                        break
                    else:
                        continue 
                #NÃO CAPTURAR    
                elif escolha_caverna == 2: 
                        print("\nSaindo...")
                        break
                else: #ESCOLHA UMA OPÇÃO VÁLIDA
                    print("\nEscolha uma opção válida!\n")
                    continue
    

    #ENTRA NA FLORESTA
    if escolha == 2:
        print("\n\nEscolheu entrar na floresta")
        #POKEMONS MATO
        lista_pokemons_mato = ["Bulbasaur", "Golduck", "Charizard"]
        pokemon_encontrado = None
        #Looping para decidir qual pokemon vai encontrar
        while True:
            pokemon_mato = random.randint(0,10)
            if 0 <= pokemon_mato <= 6: #60% de chance de capturar o Bulbasaur 
                    pokemon_encontrado = lista_pokemons_mato[0]
                    break
            elif 7<=pokemon_mato<=9: #30% de chance de capturar o Golduck 
                    pokemon_encontrado = lista_pokemons_mato[1]
                    break
            elif pokemon_mato == 10: #10% de chance de capturar o Charizard
                    pokemon_encontrado = lista_pokemons_mato[2]
                    break
        #Depois de definido qual pókemon o usuário encontrou, irá começar a captura
        print(f"\n-Você encontrou o {pokemon_encontrado}!-")
        #se o pokemon estiver na pókedex, não prosseguirá com a captura
        if pokemon_encontrado in pokedex: 
             print("\nVocê já tem este pókemon!\n")
             continue
        #Looping para tentar capturar o pókemon
        while True:
            escolha_mato = int(input(f"\nDeseja tentar capturar {pokemon_encontrado}?\n1- Sim\n2- Não\n\n-> "))
            #TENTAR CAPTURAR

            if escolha_mato == 1: 
                #50% de 10 para a chance de captura
                chance_captura = random.randint(0,10)
                #se variavel entre 0-5 (50% de 10) irá capturar
                if 0<=chance_captura<= 5:
                    print(f"\nPókemon {pokemon_encontrado} capturado com sucesso!\n")
                    pokedex.append(pokemon_encontrado)
                    captura += 1
                    break
                #se variável entre 6-10 (outro 50% de 10) não irá capturar
                elif 6<=chance_captura<=10:
                    print(f"\nPókemon {pokemon_encontrado} não capturado, tente novamente!")
                    tentativa_captura -= 1
                    print(f"\nTentativas restantes: {tentativa_captura}")
                    break 

            #NÃO TENTAR CAPTURAR

            elif escolha_mato == 2: 
                    print("\nSaindo...")
                    break
            
            #ESCOLHA UMA OPÇÃO VÁLIDA

            else: 
                print("\nEscolha uma opção válida!\n")
                continue
    
    #VER PÓKEDEX
    if escolha == 3:
        print(f"\nPókemons capturados:")
        for i in range(0,len(pokedex)):
            print(f"- {pokedex[i]}")

    #SAIR DO JOGO
    if escolha == 4:
        print("\nAté logo!\n")
        break