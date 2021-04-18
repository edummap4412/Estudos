 # Criar umn projeto Python
           # instalar Django :
             """
             1) digite o comando  : pip install django 
             2) digit o comando :django-admin   strartproject  Quiz .
                acessa o projeto com  comnado : cd Quiz
                b) emm seguida inicia o app com o comando : python ..\ manage.py startapp base
                c) crie um diretory chamado 'static' transfira os arquivos "assets" da pasta para ele
                d) acesse o servidor com o comando :  python manage.py runserver
                        use o caminho : numero_do_servidor/static/base/index.html
  
             """
            # Passar Página para página principal
                """
                a importancia do django é que ele faz a leitura do protocolo Http para facilitar
                nossa vida, o protocolo basicamente trabalha com Resquisao e resposta . com a função 
                vamos criar uma requisição no parametro de retornar uma respostaa
                 
                 1) Crie uma pasta templates 
                        dentro crie uma pasta com mesmo nome da aplicação "base"
                                Em seguida copie o arquivo 'index.html' para dentro de base.
                                    Altere o nome para "home.html
                 1)Na pasta views crie uma função home e retorn a resposta com nome da aplicação 
                            ('base', 'home.html)<nome do arquivo da base de templates
                 2)N pasta URLS. crie um path onde contem views.home(função)
                        Em seguida import um bibliteca .views( ou quiz.base import views)
                        
                """

             # Colocando CSS
                """
                  1) Vá em 'home.html' dentro entre href="./assets/styles/app.css"
                        altere usando novamente o nome das pasta static/base ficando:
                                            href="/static/base/assets/styles/app.css"
                                                 
                """
             # Criando Perguntas
                  """"
                  1) Copie a pasta game.html para templates/base
                         Path para 'perguntas e defina a função. nesse caso
                        como vamos usar um numero de paginas que nao sabemos ,use o comando :
                             'perguntas<int:indice>' ou seja:
                             '<>' pois nao sabemos quantos serao 
                             'int' para indicar o tipo de variavel
                             'indice' para dizer onde vai essa variavel
                   2) Para alterar esse Css muda da mesma maneira indicando o /static/base
                        além de alterar hef deve alterar Src no final do game.html 
                  """
            # Alterando os números da Questao
                    """
                    1) no cabeçalho 'Questao , abrimos '{{}}' duplos, dentdo deles daremos 
                    uma chave de um dict
                        Em seguida vamos para views, adicionamos mais um paramtro na função pergunta
                        (no caso :"indice") e abrimos um dicionario chamado contexto , nele colocamos 
                        a Key e depois o paramtro quue sera o valor (no caso indice).
                        
                    E para "Classiicação"(copia do arquivo end.html) segue as mesmas coniguração , criar funcao , alterar o Css e criar o Path
    
                    """
            # Criando as Perguntas:
                    """
                    Django tem um modo chamado MTV (os modelos serao criados modelos em Models esse modulo
                    facilita a comunicação entre Codigo Python e o Banco de Dados:
                        para criar o modelo :
                        1) Crie uma 'class' 
                        de o nomedo do modelo ' Pergunta de depois Herda uma classe chamda 'models.Model':
                        
                        2)para modelar o enuniciado vamos definir o tipo de dado:
                            models.TextField() =  Permite ter um tamnho de texto arbritrario
                            models.JSONField() =Permite ter um a hierarquia dos campos
                            models.BooleanField
                     """
            # Admin:
            """
              1)para criar um tabela no banco de dados
              usamos o comando : "python  manage.py migrate"
               ele intropecta os modelos que existem no Django e cria uma tabela
                
                2) Para criar um usuario digite  o comando : python manage.py createsuperuser
                     digite usuario e senha:
                3) para registar em admin os modelos:
                 use o comando "@admin.register" entao voce importa a 
                 bibloteca models ( digite as iniciais da palavra e Ctrl+ Espaço+Espaço)assim ele fara o import 
                 automatico.
                        em seguida cria uma class , geralmente criase o nome do modelo+Admin e 
                        ira herar (admin.ModelsAdmin)
                                Por fim digite pass para encerrar o preenchimento
                4) use o comando : python manage.py makemigrations nesse voce cria um arquivo em migrations
                onde ele vai migrar todo o model para formado a ser lido pelo banco de dados.
                            Em seguida use : python manage.py migrate para aplicar a migração.
    
                 5) em seguida va em admin> Perguntass>Add+perguntas
                  escreva a pergunta e depois adicione as alternativas usando 
                  esse codigo : {"array": ["function", "def", "func", "foo"]} e marque como disponivel
                  
                 6) Para mudar o Object_question(1) , vá em modelos e crie um def :
                        def __str__(self):
                            return self.enunciado (que é oque voce quer mostrar
                
                        Para criar uma lista com  cabelho como por exemplo ('id','enunciado' ,'disponivel')
                        Vá em Admin use o comando :
                            list_display = ('id', 'enunciado', 'disponivel')
                    
                 7) para azer o enunciado aparcecer va em game.html 
                 use o comando para mostrar o ''{{pergunta.enunciado}}
                 é seguida import uma biblioteca de models para views
                 e adicione o models 'perguntas.objects' na def 'perguntas'
                 
                 8) para que ele pegue somente as perguntas disponiveis use:
                 o metodo .filter(disponivel)
                 entao fica : perguntas.objects.filter(disponivel = True)
                 
                 9) para ordenar os 'id' usamos o comando order_by
                 10) em seguida pega use o comando indice com a mesma sintaxe
                  acesso de elementos de uma lista
                    detalhe  que o indice em Python começa em 0 entao use: [indice -1]
                    codigo fica: pergutas.ojects.filter(dispovicel = True).order.by('id)[inidice-1]
                    
                11) para que o game.html leia é preciso passar um contexto de memso nome que foi colocado no nas {{}}
                do arquivo
                
                12) Fazer um luppin for usando o campo Alternativas la do admin comando ficara:
                                 {%for alternativa in pergunta.alternativas.array %}
                    <div class="choice-container">
                        <p class="choice-prefix">A</p>
                        <p class="choice-text">copy</p>
                    </div>
                    {%endfor %}
                                para importar as opções:
                              <p class="choice-text">copy</p>
                    substitua o 'copy' por alternativa , justamente a variavel pedida
                                para importar as alternativas:
                                <p class="choice-prefix">A</p>
                                substitua o "A" pelo comando cycle:
                                ficando : {%cycle 'A' 'B' 'C' 'D'%}
 
            """
            #Formularios e Cadastro de Elementos
                """
                Va em home Quando quer enviar dados no Html usa a etiquueta:
                 <form class="login-form" action="game.html">
                 quando se envia dados para um servidor voce usa o metedo
                 post:  
                  <form class="login-form" method= 'post' action="game.html">
                  actiion indica como ele será enviado usando '/' vbamos enviar para a raiz
                  do projeto para tratar o recebimento deles
                  
                  altere:
                  <form class="login-form" method="post" action="/">
                  <input type="text" name ="nome" placeholder="NOME"/>
                  <input type="email" name="nome" placeholder="EMAIL"/>
                  <button type="submit">Entrar</button>
                     
                     use name = para colocar os nomes das propriedades onde sao enviadas os valores
                     submit = tipo que submete dados do formularios para o servidor
                     
                   2) use esse codigo quando aparece na pagina quando da erro : {% csrf_token %}
                   adicionando abaixo do formulário
            
                """