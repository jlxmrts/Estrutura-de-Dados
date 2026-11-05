
# Variaveis globais
global dados, MAX, ponteiro, spos, rpos, qtd, tipo

dados = []
MAX = 0
ponteiro = -1
spos = 0
rpos = 0
qtd = 0
tipo = None


# 1. PILHA

def inicializa_pilha(maximo):
    global dados, MAX, ponteiro, tipo

    MAX = maximo
    dados = []
    ponteiro = -1
    tipo = "pilha"


def push_pilha(valor):
    global dados, ponteiro, MAX

    if ponteiro == MAX - 1:
        print("\nPilha Cheia!!!")
        return

    dados.append(valor)
    ponteiro += 1


def pop_pilha():
    global dados, ponteiro

    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return None

    valor = dados[ponteiro]
    del dados[ponteiro]
    ponteiro -= 1

    return valor


def show_pilha():
    global dados

    if ponteiro < 0:
        print("\nPilha Vazia!")
    else:
        print("\nConteudo da pilha:", dados)


# 2. FILA

def inicializa_fila(maximo):
    global dados, MAX, spos, rpos, tipo

    MAX = maximo
    dados = []
    spos = 0
    rpos = 0
    tipo = "fila"


def push_fila(valor):
    global dados, spos, rpos, MAX

    if spos == MAX:
        if rpos == spos:
            dados = []
            spos = 0
            rpos = 0
        elif rpos > 0:
            dados = dados[rpos:spos]
            spos = len(dados)
            rpos = 0

    if spos == MAX:
        print("\nFila Cheia!")
        return

    dados.append(valor)
    spos += 1


def pop_fila():
    global dados, spos, rpos

    if rpos == spos:
        print("\nFila Vazia!")
        return None

    valor = dados[rpos]
    rpos += 1

    if rpos == spos:
        dados = []
        spos = 0
        rpos = 0

    return valor


def show_fila():
    global dados, spos, rpos

    if rpos == spos:
        print("\nFila Vazia!")
    else:
        print("\nConteudo da fila:", dados[rpos:spos])


# 3. FILA CIRCULAR

def inicializa_fila_circular(maximo):
    global dados, MAX, spos, rpos, qtd, tipo

    MAX = maximo
    dados = []

    for i in range(MAX):
        dados.append(None)

    spos = 0
    rpos = 0
    qtd = 0
    tipo = "circular"


def push_circular(valor):
    global dados, spos, qtd, MAX

    if qtd == MAX:
        print("\nFila Circular Cheia!")
        return

    dados[spos] = valor
    spos = (spos + 1) % MAX
    qtd += 1


def pop_circular():
    global dados, rpos, qtd, MAX

    if qtd == 0:
        print("\nFila Circular Vazia!")
        return None

    valor = dados[rpos]
    dados[rpos] = None

    rpos = (rpos + 1) % MAX
    qtd -= 1

    return valor


def show_circular():
    global dados, rpos, qtd, MAX

    if qtd == 0:
        print("\nFila Circular Vazia!")
        return

    print("\nConteudo da fila circular:")

    for i in range(qtd):
        posicao = (rpos + i) % MAX
        print(dados[posicao], end=" ")

    print()



# 4. Funções de armazenamento


def armazenar():
    global tipo

    valor = int(input("\nDigite o valor que deseja armazenar: "))

    if tipo == "pilha":
        push_pilha(valor)

    elif tipo == "fila":
        push_fila(valor)

    elif tipo == "circular":
        push_circular(valor)


def extrair():
    global tipo

    if tipo == "pilha":
        valor = pop_pilha()

    elif tipo == "fila":
        valor = pop_fila()

    elif tipo == "circular":
        valor = pop_circular()

    if valor is not None:
        print("\nValor extraido:", valor)


def imprimir():
    global tipo

    if tipo == "pilha":
        show_pilha()

    elif tipo == "fila":
        show_fila()

    elif tipo == "circular":
        show_circular()


# 5. Ordenação

def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):

            if vetor[j] > vetor[j + 1]:
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux


def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[menor]:
                menor = j

        aux = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = aux


def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave


# prepara os dados 

def obter_dados():
    global dados, tipo, ponteiro, spos, rpos, qtd, MAX

    if tipo == "pilha":
        return dados.copy()

    elif tipo == "fila":
        return dados[rpos:spos].copy()

    elif tipo == "circular":
        valores = []

        for i in range(qtd):
            posicao = (rpos + i) % MAX
            valores.append(dados[posicao])

        return valores


def atualizar_dados(vetor):
    global dados, tipo, ponteiro, spos, rpos, qtd, MAX

    if tipo == "pilha":
        dados = vetor.copy()
        ponteiro = len(dados) - 1

    elif tipo == "fila":
        dados = vetor.copy()
        rpos = 0
        spos = len(dados)

    elif tipo == "circular":
        dados = []

        for i in range(MAX):
            dados.append(None)

        for i in range(len(vetor)):
            dados[i] = vetor[i]

        rpos = 0
        qtd = len(vetor)
        spos = qtd % MAX


# 7. menu


def menu_ordenar():
    global tipo

    if tipo is None:
        print("\nCrie primeiro uma Pilha, Fila ou Fila Circular!")
        return

    while True:
        print("\n===== MENU ORDENAR =====")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao Menu Anterior")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "4":
            break

        elif opcao in ["1", "2", "3"]:

            vetor = obter_dados()

            if opcao == "1":
                bubble_sort(vetor)
                print("\nAlgoritmo utilizado: Bubble Sort")

            elif opcao == "2":
                selection_sort(vetor)
                print("\nAlgoritmo utilizado: Selection Sort")

            elif opcao == "3":
                insertion_sort(vetor)
                print("\nAlgoritmo utilizado: Insertion Sort")

            atualizar_dados(vetor)

            print("Valores ordenados com sucesso!")
            imprimir()

        else:
            print("\nOpcao invalida!")



def menu_estrutura(estrutura):

    while True:
        print("\n===== MENU", estrutura.upper(), "=====")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteudo")
        print("5 - Voltar ao Menu Anterior")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":

            maximo = int(input("\nDigite o tamanho da estrutura: "))

            if maximo <= 0:
                print("\nO tamanho deve ser maior que zero!")
                continue

            if estrutura == "pilha":
                inicializa_pilha(maximo)

            elif estrutura == "fila":
                inicializa_fila(maximo)

            elif estrutura == "circular":
                inicializa_fila_circular(maximo)

            print("\nEstrutura criada com sucesso!")

        elif opcao == "2":

            if tipo != estrutura:
                print("\nCrie a estrutura primeiro!")
            else:
                armazenar()

        elif opcao == "3":

            if tipo != estrutura:
                print("\nCrie a estrutura primeiro!")
            else:
                extrair()

        elif opcao == "4":

            if tipo != estrutura:
                print("\nCrie a estrutura primeiro!")
            else:
                imprimir()

        elif opcao == "5":
            break

        else:
            print("\nOpcao invalida!")


# 9. MENU PRINCIPAL

while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1 - PILHA")
    print("2 - FILA")
    print("3 - FILA CIRCULAR")
    print("4 - ORDENAR")
    print("5 - SAIR")

    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        menu_estrutura("pilha")

    elif opcao == "2":
        menu_estrutura("fila")

    elif opcao == "3":
        menu_estrutura("circular")

    elif opcao == "4":
        menu_ordenar()

    elif opcao == "5":
        print("\nPrograma encerrado!")
        break

    else:
        print("\nOpcao invalida!")