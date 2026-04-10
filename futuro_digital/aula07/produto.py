class Produto:
    def __init__(self, nome, preco):
        self.nome = nome # Aqui é um atributo publico
        self.preco = preco # Aqui chamamos o 'setter' mesmo dentro do construtor


    # --- O SETTER ---
    @preco.setter
    def preco(self, valor):
        """Documentação: Valida se o preço é positivo antes de atribuir."""
        if valor < 0:
            print("Erro: O preço não pode ser negativo!")
            self._preco = 0 # Usa o _ para evitar recursão infinita
        else:
            print(f"Definindo preço para: {valor}")
            self._preco = valor 


    # --- O GETTER ---
    @property
    def preco(self):
        return self.preco
