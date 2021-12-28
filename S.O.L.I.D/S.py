
class SistemaCadastral:

    def cadastrar(self, nome, idade,genero) -> None:
        if VerificaCadastro.mostra_nome and VerificaCadastro.mostra_idade and VerificaCadastro.verifica_genero:
            print(f'Cadastrar o Usuario: {nome}, Idade: {idade}, genero :{genero}')
            SalvandoNoBanco.salvando_dados(nome, idade, genero)


class VerificaCadastro:

    def verifica_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError('Valor não é uma string')

        return True

    def verifica_idade(self, idade):
        if not isinstance(idade, int):
            raise TypeError('Valor não é um inteiro')

        return True

    def verifica_genero(self, genero):
        if not 'MF':
            raise ValueError('Digite M ou F')

        return True

    @property
    def mostra_nome(self):
        return self.verifica_nome

    @property
    def mostra_idade(self):
        return self.verifica_idade


class SalvandoNoBanco:
    def __init__(self):
        self.salva_dados = []

    def salvando_dados(self, nome, idade, genero) :
        dados = {'nome': nome, 'idade': idade, 'genero': genero}

        self.salva_dados.append(dados)
        self.salva_dados.save()
        return self.salvando_dados

    @property
    def mostra_dados(self):
        return self.salva_dados

    def messagem_sucesso(self):
        return 'Cadastro feito com sucesso'

    def messagem_falha(self):
        print('Falha no cadastro , verifique os campos digitados')


usuario = SistemaCadastral()
usuario.cadastrar('Eduardo', 28, 'M')

print(usuario)