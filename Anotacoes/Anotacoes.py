#  1  Criar o projeto

    # Abra o terminal e instale o Django : pip install django
    # Abra o terminal e de o comando : pip freeze > requirements.txt
        # ( Server para instalar biblitecas da mesma versao para nao dar conflitos
            #salvando os arquivos em txt)
    # No Terminal e digite o comando : django-admin startproject django2.
    # Em seguida
        """1) Vá em Installed_apps e defina o nome da aplicação (nesse caso: 'nucleo'
           2)No campo de urls.py ( DO PROJETO) na bibloteca "django.urls" adiciona-se um modulo "include".
           Crie um 'Path' (path(''.include(nucleo.urls))
           3)dentro da pasta do projeto crie um file 'Python Package que será a APP(nucleo) do programa
           4)Cria um arquivo python para dentro da pasta "urls.py"
           5)Dentro de views.py definimos as funções
           6)Dentro de urls(DA APLICAÇÃO) definimos a biblioteca django.urls com modulo 'path'
            e uma nova biblioteca .views  com modulo das funcoes definidas anteriormente
            7) Va em  TEMPLATES (settings) e no campo DIRS : escreva 'templates'
            8)cria um diretory com o mesmo nome.
            9)crie um arquivo HTML com o nome da funções (que estão em .views)"""
        #Models(converte arquivos de banco de dados para arquivos Python , deixando mais facil)ps:eduardo do futuro, eu sei..
            """10)Crie um models (ou seja criar um Class)(ignore Def por enquanto) e 
            digite o comando : !"python manage.py makemigrations" (cria um banco de dados)
                11) para excutar Aplicação insira : python manage.py migrate
            """
        # Area administrativa
                """No Django existe o comando admin que cria uma area administrativa com campos usuario e senha """
                """12 ) digite o comando : python manage.py createsuperuser
                   13 ) Quando criado a super usuario , aparece admin.py" la voce vai importar uma bibloteca
                   de .models para que seus modelos(da sua aplicação sejam aplicados no site).
                    
                       * Para mudar nome que aparece "product" voce cria uma Def(função) str para retornar nome digitado
                       
                       * Para que apareça as informações mais informacoes onde aparece "product" voce precisa ir em 
                         admin.py importar um class .
                   """
            #Shell
                """
                 Possível adicionar mais itens tanto em 'Podutos quanto em Clientes atraves do Terminal python
                    digite : python manage.py  shell
                 1) digite : from nucleo.models import Costumer
                 2) digite : costumer = Costumers(nome='Eduardo',sobrenome ='Mascarenhas",email = Eduardomichael@python.com)
                 3) digite : costumer.save()
                    Para verificar se funcionou:
                        digite: costumer.pk e depois costumer.id
                4) para fazer alterações :
                    digite: "costumer.nome="  ou o campo de desejar mudar. e digite o nome alterado
                 5) para deletar o objeto : costumer.delete()   
                 
                        6)Dando comando dir(Produto) no terminal vemos as possibilidades do mesmo
                        ex :
                         Produto.objects.all() = ver todos os itens de 'Produto'
                         digite : >>> produto
                         
                         Produto.objects.count() = contar quantos produtos tem .
                         Produto.objects.first() = mostra o primeiro objeto
                         Produto.objects.filter(id=(numero)) = mostra o produto nesse campo
                         
                """
            # Request  no views:
                """
                        1)em baixo da função index faça um :
                            print(dir(request.user))
                            print(f'User: {request.user}'ele mostrará as funções do Request
                        2) Delogando de Admin  e usando o metodo acima: ira printar no USER : ANONYMOUSUSER. copie esse nome
                        e jogue essa logica abaixo do def index identado:
                             if str(request.user) == 'AnonymousUser':
                                    teste = 'Usuário não logado'
                            else:
                                    teste = 'Usuário LOGADO'         
                            dentro de contex : crie uma Key : 'logado': teste
                        3) vá para Templates em index:
                                crie um paragrafo
                                
                    """

    # MIDDLEWARE
        """Quando o sisteme recer uma requisição MIDDLEWARE vai checar quem é o usuario ou se esta logado , verificar
            a segurança e podemos criar nosso proprios MIDDLEWARE"""

    #WSGI_ APPLICATION
        "Padrão de aplicação Python"

    # DATABASE
        " O python3 já tem o SQLite3 como padrao mas tambem passa como usar outros DB"

    # ATUH_PASSWORD_VALIDATORS
        "UM VALIDADDOR DE SENHAS...."

