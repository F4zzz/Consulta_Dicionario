import requests
print('#'*19)
print('## DICIONARIO F4 ##')
print('#'*19)
def inicio():
    print('''O que deseja fazer? 
    [1] Consulta Rápida
    [2] Consulta Detalhada
    [3] Sair
    ''')
    escolha = int(input('Digite uma opção: ').strip())
    if escolha == 1:
        rapida()
    elif escolha == 2:
        detalhada()
    else:
        print('Programa encerrado...')
        print('Volte sempre :) ')
        exit()
def dnv():
    quest = input('Realizar nova consulta? [Sim/Nao] ').strip().lower()
    if quest == 'sim':
        inicio()
    else:
        print('Programa encerrado...')
        print('Volte sempre :) ')
        quit()
def rapida():
    palavra = input('Digite a palavra: ').strip()
    url = f"https://significado.herokuapp.com/{palavra}"
    res = requests.get(url)
    data = res.json()
    if res:
        print(f'-> Palavra: {palavra}')
        print(f'-> Significado: {data[0]["meanings"][0]}')
    else:
        print('Essa palavra não existe :(')
    dnv()
def detalhada():
    palavra = input('Digite a palavra: ').strip()
    url = f"https://significado.herokuapp.com/{palavra}"
    res = requests.get(url)
    data = res.json()
    url2 = f"https://significado.herokuapp.com/synonyms/{palavra}"
    res2 = requests.get(url2)
    data2 = res2.json()
    if res:
        print(f'''
-> Palavra: {palavra}
-> Classe: {data[0]["class"]}
-> Significados: {data[0]["meanings"]}
-> Sinônimos: {data2}
-> {data[0]["etymology"]}
''')
    else:
        print('Essa palavra não existe :(')
    dnv()
inicio()
