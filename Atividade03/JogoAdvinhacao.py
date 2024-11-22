import json

class JogoAkinator:
    def __init__(self, arquivo_json):
        # Carregar os personagens a partir do arquivo JSON
        with open(arquivo_json, 'r') as f:
            self.personagens = json.load(f)
        
        # Inicializando a árvore de decisão
        self.perguntas = self.criar_arvore_decisao()

    def criar_arvore_decisao(self):
        """
        Cria uma árvore de decisão com base nas características dos personagens.
        Cada nó é uma pergunta e as folhas são os personagens.
        """
        perguntas = {
            'animacao': {
                'sim': {
                    'superpoder': {
                        'sim': {
                            'nome': 'Homem-Aranha'
                        },
                        'nao': {
                            'nome': 'SpongeBob'
                        }
                    }
                },
                'nao': {
                    'superpoder': {
                        'sim': {
                            'nome': 'Batman'
                        },
                        'nao': {
                            'nome': 'Mulher Maravilha'
                        }
                    }
                }
            }
        }
        return perguntas

    def jogar(self):
        """
        Inicia o jogo, fazendo perguntas até adivinhar o personagem ou até o usuário desistir.
        """
        self.faz_pergunta(self.perguntas)

    def faz_pergunta(self, node):
        """
        Função recursiva que percorre a árvore de decisão até encontrar o personagem ou até o usuário desistir.
        """
        if 'nome' in node:
            print(f"Eu acho que o personagem é: {node['nome']}")
            resposta = input("Isso está correto? (sim/não): ").strip().lower()
            if resposta == 'sim':
                print("Eu acertei!")
            else:
                print("Hmm... Eu errei. Talvez na próxima!")
            return
        
        for pergunta, resposta in node.items():
            resposta_usuario = input(f"Seu personagem é {pergunta}? (sim/não): ").strip().lower()
            if resposta_usuario == 'sim':
                self.faz_pergunta(resposta['sim'])
            elif resposta_usuario == 'nao':
                self.faz_pergunta(resposta['nao'])

# Iniciar o jogo
if __name__ == "__main__":
    jogo = JogoAkinator("personagens.json")
    jogo.jogar()
