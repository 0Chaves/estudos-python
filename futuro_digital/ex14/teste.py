from livro import Livro
from narrador import Narrador
from audio_livro import Audio_Livro
from editora import Editora

if __name__ == "__main__":  
    # Criando uma editora
    editora1 = Editora(nome="Editora ABC", cnpj="12.345.678/0001-90")

    # Criando um livro
    livro1 = Livro(titulo="O Senhor dos Anéis", ano=1954, autor="J.R.R. Tolkien", isbn="978-0544003415")
    livro1.definir_editora(editora1)

    # Criando um narrador
    narrador1 = Narrador(nome="Carlos Silva", sexo="Masculino")

    # Criando um audiolivro
    audio_livro1 = Audio_Livro(titulo="O Senhor dos Anéis - Audiolivro", ano=1954, autor="J.R.R. Tolkien", isbn="978-0544003415", narrador=narrador1, tempoLeitura=20)
    audio_livro1.definir_editora(editora1)

    # Testando a reprodução do livro
    livro1.reproduzir()

    # Testando a reprodução do audiolivro
    audio_livro1.reproduzir()