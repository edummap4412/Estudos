

class Cliente():
    def __init__(self, nome_completo, endereco, email):
        self.nome_completo = nome_completo
        self.endereco = endereco
        self.email = email

    @property
    def dados(self):
        return self.nome_completo, self.endereco, self.email


class Banco(Cliente):
    def __init__(self, dados : Cliente, conta, saldo):
        self.dados = dados
        self.conta = conta
        self.saldo = saldo

    def tipo_conta(self,tipo):
        return tipo

    def lista_dados(self, dados):
        return


dados_cliente = Cliente('Eduardo Michael Mascarenhas Pereira',
                        'Rua Canfudé do Judas',
                        'eduardo@eduardo.com')
print(dados_cliente.dados)

cliente_banco = Banco(dados_cliente.dados,123, 200)

cliente_banco.da