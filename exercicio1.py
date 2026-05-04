class No:
    def __init__(self, codigo, nome_cliente, descricao_pedido, pedido_agendado):
        self.codigo = codigo
        self.nome_cliente = nome_cliente
        self.descricao_pedido = descricao_pedido
        self.pedido_agendado = pedido_agendado
        self.prox = None
        self.ant = None

    # define como o nó será exibido no print
    def __str__(self):
        return f"Código: {self.codigo}, Cliente: {self.nome_cliente}, Descrição: {self.descricao_pedido}, Agendado: {self.pedido_agendado}"


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def inserir_final(self, codigo, nome_cliente, descricao_pedido, pedido_agendado):
        novo_dado = No(codigo, nome_cliente, descricao_pedido, pedido_agendado)

        # caso a lista esteja vazia
        if self.inicio is None:
            self.inicio = novo_dado
            self.fim = novo_dado
        else:
            # inserir no final da lista
            self.fim.prox = novo_dado
            novo_dado.ant = self.fim
            self.fim = novo_dado

        self.tamanho += 1
        return "Comanda inserida no final"


    def inserir_agendado(self, codigo, nome_cliente, descricao_pedido, pedido_agendado):
        novo_dado = No(codigo, nome_cliente, descricao_pedido, pedido_agendado)
        aux = self.inicio

        # 1) caso a lista seja vazia
        if self.inicio is None:
            self.inicio = novo_dado
            self.fim = novo_dado
            self.tamanho += 1
            return "Comanda inserida (lista vazia)"

        # 2) primeiro já é normal → inserir no início
        if self.inicio.pedido_agendado is False:
            novo_dado.prox = self.inicio
            self.inicio.ant = novo_dado
            self.inicio = novo_dado
            self.tamanho += 1
            return "Comanda agendada inserida no início"

        # 3) percorrer enquanto os nós forem agendados
        while aux and aux.pedido_agendado is True:
            aux = aux.prox

        # 4) chegou ao fim da lista (todos eram agendados)
        if aux is None:
            self.fim.prox = novo_dado
            novo_dado.ant = self.fim
            self.fim = novo_dado

        # 5) encontrou o primeiro nó normal → inserir antes dele
        else:
            anterior = aux.ant
            anterior.prox = novo_dado
            novo_dado.ant = anterior

            novo_dado.prox = aux
            aux.ant = novo_dado

        self.tamanho += 1
        return "Comanda agendada inserida com sucesso"


    def remover_por_codigo(self, codigo):
        aux = self.inicio

        # 1) buscar o nó pelo código
        while aux and aux.codigo != codigo:
            aux = aux.prox

        # 2) se não encontrou
        if aux is None:
            return "Comanda não encontrada"

        # 3) se é o único nó
        if aux == self.inicio and aux == self.fim:
            self.inicio = None
            self.fim = None

        # 4) se é o primeiro nó
        elif aux == self.inicio:
            self.inicio = aux.prox
            self.inicio.ant = None

        # 5) se é o último nó
        elif aux == self.fim:
            self.fim = aux.ant
            self.fim.prox = None

        # 6) se está no meio
        else:
            anterior = aux.ant
            posterior = aux.prox
            anterior.prox = posterior
            posterior.ant = anterior

        self.tamanho -= 1
        return "Comanda removida com sucesso"


    def alterar_descricao(self, codigo, nova_descricao):
        aux = self.inicio

        # 1) buscar o nó pelo código
        while aux and aux.codigo != codigo:
            aux = aux.prox

        # 2) se encontrou → altera o atributo
        if aux is not None:
            aux.descricao_pedido = nova_descricao
            return "Descrição alterada com sucesso"

        # 3) se não encontrou
        else:
            return "Comanda não encontrada"


    def exibir_atual(self):
        aux = self.inicio

        # caso a lista esteja vazia
        if aux is None:
            return "Nenhuma comanda cadastrada"
        resultado = ''
        #utilizei o método str() para quando eu retornar o aux me aparecer o
        #resultado e não o endereço de memória
        while aux:
            resultado += f'{aux.codigo} - {aux.nome_cliente}\n'
            aux = aux.prox

        return resultado

    #método de ver quantas comandas eu tenho no varal
    def comandas_ativas(self):
        return f"Quantidade de comandas ativas: {self.tamanho}"



def gerar_menu():
    print("\n[1] Alterar descrição")
    print("[2] Remover comanda")
    print("[3] Exibir comandas")
    print("[4] Quantidade de comandas")
    print("[5] Sair")


def main():
    comanda = ListaDuplamenteEncadeada()

    qtd = int(input("Qual a quantidade de pedidos? "))

    # cadastro inicial das comandas
    for _ in range(qtd):
        codigo = int(input("Código: "))
        nome_cliente = input("Nome do cliente: ")
        descricao_pedido = input("Descrição: ")
        resposta = input("É agendado? ").lower()

        # validação da resposta
        while resposta not in ["sim", "nao", "não"]:
            resposta = input("Digite sim ou não: ").lower()

        # decisão de inserção
        if resposta == "sim":
            print(comanda.inserir_agendado(codigo, nome_cliente, descricao_pedido, True))
        else:
            print(comanda.inserir_final(codigo, nome_cliente, descricao_pedido, False))

        print()

    # menu interativo
    while True:
        print('\n----------------------------')
        print(f'--MENU DE VARAL DE COMANDAS--')
        gerar_menu()
        opcao = int(input("Escolha uma opção: "))

        print()
        match opcao:
            case 1:
                codigo = int(input("Código: "))
                nova = input("Nova descrição: ")
                print(comanda.alterar_descricao(codigo, nova))

            case 2:
                codigo = int(input("Código: "))
                print()
                print(comanda.remover_por_codigo(codigo))

            case 3:
                print(comanda.exibir_atual())

            case 4:
                print(comanda.comandas_ativas())

            case 5:
                print("Encerrando...")
                break

            case _:
                print("Opção inválida")

        print('----------------------------\n')


if __name__ == "__main__":
    main()