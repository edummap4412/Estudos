"""
Métodos Mágicos

Métodos Mágicos, são todos os médotos que utilizam dunder


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        " Representa métodos para o usúario."
        return self.titulo

    def __repr__(self):
        " Representa métodos para o dev."
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Um objeto do tipo {self.titulo}  foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        "Retornar  opação aritimética"
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!','Geek University', 400)
livro2 = Livro('Dom Quichote','Escritor', 500)

print(livro1)
print(livro2)

print(livro1 + livro2)