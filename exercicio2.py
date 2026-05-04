from collections import deque

class Caixa:
    def __init__(self):
        #estrutura que guarda os itens (deque)
        self.itens = deque()
        self.camadas = {
            "base": ["molhos", "farofa", "cumbuca de feijoada", "feijão extra"],
            "intermediario": ["bisteca", "paio", "torresmo", "bacon"],
            "superior": ["arroz", "couve", "mandioca", "banana"],
            "topo": ["laranja", "caipirinha"]
        }
        # Define a ordem hierárquica das camadas (do fundo ao topo)
        self.ordem_camadas = ["base", "intermediario", "superior", "topo"]
        # Inicializado para evitar AttributeError caso qtd_itens_removidos()
        # seja chamado antes de qualquer correção
        self._itens_removidos_ultima_correcao = 0

    def empilhar_novo_item(self, item):
        camada_item = self.descobrir_camada(item)

        if camada_item is None:
            return f"'{item}' não é um item válido"

        camada_atual = self._camada_mais_alta_na_pilha()

        if camada_atual is not None:
            idx_novo = 0
            idx_atual = 0
            posicao = 0

            for camada in self.ordem_camadas:
                if camada == camada_item:
                    idx_novo = posicao

                if camada == camada_atual:
                    idx_atual = posicao

                posicao += 1

            if idx_novo < idx_atual:
                return (
                    f"'{item}' pertence à camada '{camada_item}', mas a caixa "
                    f"já possui itens da camada '{camada_atual}'. "
                    f"Não é possível adicionar itens de camadas anteriores."
                )

        self.itens.append(item)
        return f"'{item}' adicionado ao topo da caixa (camada: {camada_item})"

    def desempilhar_item_topo(self):
        if self.itens:
            retirado = self.itens.pop()
            return f"'{retirado}' retirado do topo"
        else:
            return "Pilha vazia"

    def exibir_atual(self):
        if not self.itens:
            return "A caixa está vazia"

        else:
            for i in range(len(self.itens)):
                item = self.itens[i]
                if i == len(self.itens) - 1:
                    print(f"{item} (TOPO)")
                else:
                    print(item)

    # Optaei na correção da PILHA por não oferecer a opção de inserção, e apenas desmontar a pilha,
    # excluir o item defeituoso e armazenar a quantidade de itens removidos
    def corrigir_montagem(self, item):
        if not self.itens:
            return 'A caixa está vazia'

        if item not in self.itens:
            return f"'{item}' não existe na caixa"

        removidos = 0
        retirados = []

        # Retirar do topo até chegar no item
        while self.itens and self.itens[-1] != item:
            retirado = self.itens.pop()
            retirados.append(retirado)
            removidos += 1

        # Ao encontrar o elemento, retira o próprio item defeituoso
        self.itens.pop()

        self._itens_removidos_ultima_correcao = removidos

        if retirados:
            sequencia = ""
            primeiro = True

            for retirado in retirados:
                if primeiro:
                    sequencia = sequencia + retirado
                    primeiro = False
                else:
                    sequencia = sequencia + " -> " + retirado
        else:
            sequencia = "(nenhum item acima)"

        return (
            f"Itens retirados: {sequencia}\n"
            f"'{item}' retirado para correção\n"
        )


    # Impressão de quantos itens foram removidos durante a última correção
    def qtd_itens_removidos(self):
        return f"Quantidade de itens removidos na última correção: {self._itens_removidos_ultima_correcao}"

   # Retorna a camada mais alta presente na pilha atual.
    # Usada para impedir adição de itens de camadas inferiores.
    def _camada_mais_alta_na_pilha(self):
        camada_mais_alta = None

        # passando por cada item da pilha
        for item in self.itens:
            camada = self.descobrir_camada(item)

            if camada is not None:
                posicao_camada = 0
                posicao_camada_mais_alta = 0

                for i in range(len(self.ordem_camadas)):
                    if self.ordem_camadas[i] == camada:
                        posicao_camada = i

                    if camada_mais_alta is not None and self.ordem_camadas[i] == camada_mais_alta:
                        posicao_camada_mais_alta = i

                if camada_mais_alta is None or posicao_camada > posicao_camada_mais_alta:
                    camada_mais_alta = camada

        return camada_mais_alta


    # Retorna o nome da camada em que o item está. Para itens sem camada, retorna None.
    def descobrir_camada(self, item):
        for camada, lista in self.camadas.items():
            if item in lista:
                return camada
        return None

    # Valida se o item existe em alguma camada
    def validar_item(self, item):
        return self.descobrir_camada(item) is not None


def gerar_menu():
    print("\n[1] Empilhar Novo Item")
    print("[2] Desempilhar Item ")
    print("[3] Exibir Estado Atual")
    print("[4] Corrigir Montagem")
    print("[5] Quantidade de Itens Removidos")
    print("[6] Sair")

# main() - função principal
def main():
    caixa = Caixa()

    while True:
        gerar_menu()
        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido")
            continue

        match opcao:
            case 1:
                item = input("Qual item você quer colocar na pilha? ").lower()
                print(caixa.empilhar_novo_item(item))

            case 2:
                print(caixa.desempilhar_item_topo())

            case 3:
                caixa.exibir_atual()

            case 4:
                item = input("Qual item você quer encontrar? ").lower()
                print(caixa.corrigir_montagem(item))

            case 5:
                print(caixa.qtd_itens_removidos())

            case 6:
                print("Encerrando...")
                break

            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()