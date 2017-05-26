# Encurta URL
Projeto feito em Django para encurtar URL's

Instalação:

1 - Clonar o repositório:

$ git clone https://github.com/alisonamerico/encurtaurl-alisonamerico.git

2 - Acessar pasta:

$ cd encurtaurl-alisonamerico

3 - Criar um ambiente virtualenv:

$ virtualenv encurtaurl-alisonamerico -p python3

4 - Acessar subpasta:

$ cd encurtaurl-alisonamerico

5 - Ativar o ambiente virtualenv:

$ source bin/activate

6 - Voltar pasta:
$ cd ..

7 - Instalar dependencias do projeto:

$ pip install -r requirements.txt

8 - É necessário criar um arquivo chamado ".env" na raíz no do projeto:

  --> Botão direito em cima de da raíz do projeto "encurtaurl-alisonamerico"
  --> New File
  --> .env
  --> Gerar uma SECRET_KEY: http://www.miniwebtool.com/django-secret-key-generator/
  --> Click em "Generate Django Secret Key"
  --> Coloque dentro do arquivo ".env" as variáveis:
        SECRET_KEY=coloque_aqui_o_valor_da_secret_key_gerada_anteriormente_sem_espaço
        DEBUG=True

9 - Realizar as migrações das tabelas:

$ python manage.py migrate

10 - Executar projeto:

$ ./manage.py runserver

11 - Informe uma URL qualquer para teste:

https://facebook.com
