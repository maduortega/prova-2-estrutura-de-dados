from collections import deque

class FilaDePedidos:

    def __init__(self):
        # Fila (FIFO) com deque, descobri que ao usarmos underline trata-se de um 
        # atributo privado, ou que não deve ser acessado fora das classes, 
        # mas apenas por suas funções.
        self._fila = deque() 

    def inserir(self, codigo, descricao_pedido, origem):
        if origem not in ("SALAO", "DELIVERY"):
            print(f'Escolha SALAO ou DELIVERY')
            return

        #preciso guardar várias informações diferentes sobre um mesmo pedido
        pedido = {
            'codigo':codigo,
            'descricao':descricao_pedido,
            'origem':origem
        }

        self._fila.append(pedido)
        #confirmação de pedido inserido aqui:
        return f'Pedido {codigo} na fila: {descricao_pedido}'

    def atender(self):
        if not self._fila:
            print('A fila está vazia!')
            return None

        #aqui acontece igual em pós-fixa, ao encontrar o elemento dei um popleft
        pedido = self._fila.popleft()

        print(f'Pedido "{pedido["codigo"]} - {pedido["descricao"]}" atendido com sucesso')

        return pedido

    def esta_vazia(self):
        return len(self._fila) == 0

    def exibir(self):
        if not self._fila:
            print("A fila está vazia")
            return

        #quantidade de pedidos
        for i in range(len(self._fila)):
            #vira o pedido atual (um dicionário)
            p = self._fila[i]

            #primeiro elemento da fila
            if i == 0:
                print(p['codigo'], "-", p['descricao'], "-", p['origem'], "<- próximo")
            else:
                print(p['codigo'], "-", p['descricao'], "-", p['origem'])

        print()

    # 5. e 6. fazem parte do mesmo processo

    def processar_todos(self):
        if self.esta_vazia():
            print('Não há dados para processar')
            return

        contagem = {
            'SALAO':0,
            'DELIVERY':0
        }

        while self._fila:
            pedido = self._fila.popleft()
            print(f"Processando '{pedido['codigo']} - {pedido['descricao']}'")
            #dicionário para contar a quantidade de pedidos de cada tipo
            contagem[pedido['origem']] += 1

        #Fim do processamento, exibir resumo
        print(f'FIM DO PROCESSAMENTO. Resumo:')
        print(f"QTD SALAO: {contagem['SALAO']}")
        print(f"QTD DELIVERY: {contagem['DELIVERY']}\n")
        return contagem


def gerar_menu():
    print("\n[1] Inserir pedido")
    print("[2] Atender pedido")
    print("[3] Verificar se a fila está vazia")
    print("[4] Exibir fila")
    print("[5] Processar todos os pedidos")
    print("[6] Sair")


def main():
    fila = FilaDePedidos()

    while True:
        gerar_menu()

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print(f'Digite um número válido')
            continue

        match opcao:
            case 1:
                codigo = int(input("Código: "))
                descricao_pedido = input("Descrição do pedido: ")
                origem = input("Origem (SALAO ou DELIVERY): ").upper()
                print(fila.inserir(codigo, descricao_pedido, origem))

            case 2:
                fila.atender()

            case 3:
                if fila.esta_vazia(): print('Está vazia')
                else: print('Não está vazia')

            case 4:
                fila.exibir()

            case 5:
                fila.processar_todos()

            case 6:
                print("Encerrando...")
                break

            case _:
                print("Opção inválida")


if __name__ == "__main__":
    main()
