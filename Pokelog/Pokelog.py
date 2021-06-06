import requests
from bs4 import BeautifulSoup

tipos = ['Aço', 'Água', 'Dragão', 'Elétrico','Fada','Fantasma','Fogo',
         'Gelo','Inseto', 'Lutador', 'Normal','Pedra','Planta','Psiquico',
         'Sombrio','Terrestre','Venenoso','Voador']

tipos_autolog = ['Steel', 'Water', 'Dragon', 'Electric','Fairy','Ghost','Fire',
         'Ice','Bug', 'Fighting', 'Normal','Rock','Grass','Psychic',
         'Dark','Ground','Poison','Flying']

#Tabela para analise de resistencias/fraquezas.
#Cada linha é um tipo e ela está odenada alfabeticamente, como a lista acima.
#É vista pela perpectiva de defesa, onde 0 é neutro, 1 é resistencia, 5 imunidade e -1 é fraqueza.
tabela=[[ 1, 0, 1, 0, 1, 0,-1, 1, 1,-1, 1, 1, 1, 1, 0,-1, 5, 1], #aço
        [ 1, 1, 0,-1, 0, 0, 1, 1, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0], #água
        [ 0, 1,-1, 1,-1, 0, 1,-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #assim por diante
        [ 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 1],
        [-1, 0, 5, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0,-1, 0],
        [ 0, 0, 0, 0, 0,-1, 0, 0, 1, 5, 5, 0, 0, 0,-1, 0, 1, 0],
        [ 1,-1, 0, 0, 1, 0, 1, 1, 1, 0, 0,-1, 1, 0, 0,-1, 0, 0],
        [-1, 0, 0, 0, 0, 0,-1, 1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 1, 0,-1, 1, 0, 0, 1, 0,-1],
        [ 0, 0, 0, 0,-1, 0, 0, 0, 1, 0, 0, 1,-1, 1, 0, 0, 0,-1],
        [ 0, 0, 0, 0, 0, 5, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1,-1, 0, 0, 0, 0, 1, 0, 0,-1, 1, 0,-1, 0, 0,-1, 1, 1],
        [ 0, 1, 0, 1, 0, 0,-1,-1,-1, 0, 0, 0, 1, 0, 0, 1,-1,-1],
        [ 0, 0, 0, 0, 0,-1, 0, 0,-1, 1, 0, 0, 0, 1,-1, 0, 0, 0],
        [ 0, 0, 0, 0,-1, 1, 0, 0,-1,-1, 0, 0, 0, 5, 1, 0, 0, 0],
        [ 0,-1, 0, 5, 0, 0, 0,-1, 0, 0, 0, 1,-1, 0, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1,-1, 0,-1, 1, 0],
        [ 0, 0, 0,-1, 0, 0, 0,-1, 1, 1, 0,-1, 1, 0, 0, 5, 0, 0]]
        
def analisar_resistencias():
    resistencias = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    for i in range(18):
        resistencias[i] += tabela[tipo1-1][i]
        
    if tipo1 != tipo2:
        for i in range(18):
            resistencias[i] += tabela[tipo2-1][i]
            
    return resistencias

def imprimir_basico():
    print(f'\npokemon({nome}).')
    if evolucao != False:
        print(f'evolução({nome},{evolucao}).') 
    print(f'tipo({nome},{tipos[tipo1-1]}).')
    if (tipo1 != tipo2):    
        print(f'tipo({nome},{tipos[tipo2-1]}).')

    
def imprimir_fraquezas(resistencias):
    for i in range(18):
        if resistencias[i] < 0:
            print(f'fraqueza({nome},{tipos[i]}).')

def imprimir_resistencias(resistencias):
    for i in range(18):
        if resistencias[i] == 1 or resistencias[i] == 2 :
            print(f'resistencia({nome},{tipos[i]}).')

def imprimir_imunidades(resistencias):
    for i in range(18):
        if resistencias[i] > 2:
            print(f'imunidade({nome},{tipos[i]}).')

def nova_entrada():
    try:
        entrada = input('Nome evolução tipo1 tipo2 (se existente) ou 0 para sair: ').split(" ")
        
        if entrada[0] == '0': #Criterio de parada
            return '0'
        
        if entrada[1].isdigit():#Verificando se não foi inserido uma evolução
            entrada.insert(1, False) #Inserindo False como evolução
        
        if not entrada[2].isdigit() or int(entrada[2]) > 18 or int(entrada[2]) < 1:#Verificando se o tipo 1 e 2 são numeros validos
            print("\nTipo invalido, use numeros conforme informado.\n")
            return nova_entrada()
        
        if len(entrada) == 4:
            if not entrada[3].isdigit() or int(entrada[3]) > 18 or int(entrada[3]) < 1:#Verificando se o tipo 1 e 2 são numeros validos
                print("\nTipo 2 invalido, use numeros conforme informado.\n")
                return nova_entrada()
        
        return entrada 
    except:
        print("\nEntrada invalida, tente novamente.\n")
        return nova_entrada()
        
def setup(): #Introduzindo e vendo do que o usuario precisa
    print("\nOlá, vejo que procura algo para catalogar pokemons para prolog!\n"
          "Posso fazer isso para você! Apenas me diga quais informações precisa e podemos começar!\n")
    setup = ['','','','',''] #[basico , fraquezas , resistencias , imunidades]
    setup[0] = input("Deseja imprimir as informações basicas? Elas são pokemon, evolução, tipos 1 e 2 (s/n): ")
    setup[1] = input("Deseja imprimir as fraquezas? (s/n): ")
    setup[2] = input("Deseja imprimir as resistencias? (s/n): ")
    setup[3] = input("Deseja imprimir as imunidades? (s/n): ")
    setup[4] = input("Deseja que eu faça todo o trabalho? (s/n): ") #Provisorio
    for i in range(5):
        if setup[i] == 's':
            setup[i] = True
        else:
            setup[i]= False
    if setup[4]:
        print("\n\nTudo certo, vamos começar! Apenas me informe de qual a qual numero de pokemon você quer catalogar!")
    else:
        print("\n\nTudo certo, vamos começar! Lembrando que você deve me informar o tipo do pokemon usando numeros:\n"
              "1-aço 2-água 3-dragão 4-eletrico 5-fada 6-fatasma 7-fogo 8-gelo 9-inseto 10-lutador\n"
              "11-normal 12-pedra 13-planta 14-psiquico 15-sombrio 16-terra 17-venenoso 18-voador.\n\n")
    return setup
    
def autolog(id_pokemon): #Precisa de internet
    
    site = "https://www.pokemon.com/br/pokedex/" + str(id_pokemon)
    r = requests.get(site) #Obtendo o HTML do site
    soup = BeautifulSoup(r.text, 'html.parser') 

    nome_encontrado = soup.find("div",attrs={"class":"pokedex-pokemon-pagination-title"}).text.split("\n      ")
    nome = nome_encontrado[1]
    
    tipos_encontrados = soup.find("div",attrs={"class":"dtm-type"}).text.split("\n\n\n")
    tipo1 = tipos_autolog.index(tipos_encontrados[1]) + 1
    if len(tipos_encontrados) == 4:
        tipo2 = tipos_autolog.index(tipos_encontrados[2]) + 1
    else:
        tipo2 = tipo1
        
    evolucao = evolucao_autolog(soup, nome)
    
    return nome, tipo1, tipo2, evolucao

def evolucao_autolog(soup, nome):
    try:
        evolucoes_encontradas = soup.find("div",attrs={"class":"column-12 push-1 dog-ear-bl"}).text.split("\n\n\n\n\n\n        ")
        evolucao = False
        
        lista_evo = []
        for i in range(1, len(evolucoes_encontradas)):
            lista_evo.append(evolucoes_encontradas[i].split('\n')[0])
        
        index_nome = lista_evo.index(nome)
        if index_nome < len(lista_evo)-1: #verificando se é o ultimo da lista
            evolucao = lista_evo[index_nome + 1]
    except:
        evolucao = False
    return evolucao


def entrada_autolog():
    try:
        inicio = int(input("Do n°"))
        fim = int(input("ao n°"))
        if fim < inicio:
            print("\n inicio maior que o fim, tente novamente.\n")
            return entrada_autolog()
        return(inicio, fim)
    except:
        print("\nEntrada invalida, tente novamente.\n")
        return entrada_autolog()
        
def saidas():
    if setup[0]:
        imprimir_basico()
    if setup[1] or setup[2] or setup[3]: #Só analisa as resistencias se necessario
        resistencias = analisar_resistencias()
    if setup[1]:
        imprimir_fraquezas(resistencias)
    if setup[2]:
        imprimir_resistencias(resistencias)
    if setup[3]:
        imprimir_imunidades(resistencias)
    print()


#main
setup = setup()
if setup[4]:
    inicio, fim = entrada_autolog()
    for id_pokemon in range(inicio, fim):
        nome, tipo1, tipo2, evolucao = autolog(id_pokemon)
        saidas()
    print("\nAviso: No momento eu tenho não consigo entender pokemons que tem arvore de evolução não-linear...\n"
          "Então confira bem as evoluções dos pokemons que você sabe que são assim!\n"
          "\nObrigado por me usar :D\n")
else:
    while True:
        entrada = nova_entrada()
        if entrada[0] == '0':
            print("\nObrigado por me usar :D\n")
            break
        nome = entrada[0]
        evolucao = entrada[1]
        tipo1 = tipo2 = int(entrada[2])
        if len(entrada) == 4:
            tipo2 = int(entrada[3])
        
        saidas()
