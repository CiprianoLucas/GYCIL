# Entra21 - Projeto Gycil
Este projeto foi desenvolvido como parte do curso Entra21, com o objetivo de desenvolver programadores. O projeto consiste em um site desenvolvido em Django, hospedado na AWS, que facilita a conexão entre prestadores de serviços de diversas categorias e clientes, tornando a contratação de serviços mais rápida e confiável.

## Integrantes do Grupo
- Lucas Henrique Cipriano;
- Igor de Pin Faggiani;
- Yuri Silva de Campos;
- Cauã Vitor Mendes;
- Guilherme Eduardo Schmoller de Souza

## Funcionalidades Principais
- Cadastro de prestadores de serviços e clientes;
- Conexão entre prestadores de serviços e clientes;
- Pesquisa de prestadores de serviços por categoria;
- Facilidade na contratação de serviços;
- Disponibilidade de arquivos para registro;

## Utilizadas
- Django; 
- AWS (Amazon Web Services); 
- HTML/CSS/Bootstrap; 
- JavaScript;
- Figma;
- Nginx;
- Trello

## Instalação

Tenha Python e pip instalado no computador

Dentro da pasta GYCIL/GYCIL, crie um arquivo .env
Se for usar banco de dados locais não é necessário preencher os campos de AWS
Se usar banco de dados da AWS coloque o ENV=production

```env
ENV=<production/development>
SECRET_KEY=secret_key_para_sua_aplicacao

# AWS
DB_NAME=<nome_banco_de_dados>
DB_USER=<nome_usuario>
DB_PASSWORD=<senha_usuario>
DB_HOST=<ip_name_host>
DB_PORT=<porta>
AWS_ACCESS_KEY_ID=id_chave_acesso
AWS_SECRET_ACCESS_KEY=senha_chave_acesso
AWS_STORAGE_BUCKET_NAME=nome_bucket

```


Clone o repositório e na pasta raiz execute os comandos:
```cmd
py -m venv venv  
.\venv\Scripts\activate
pip install -r requirements.txt
cd GYCIL
py manage.py migrate

```


para criar um super usuário utilize o comando
```cmd
py manage.py createsuperuser
```

para iniciar a aplicação web utilize o comando
```cmd
py manage.py runserver
```

Responsividade da aplicação para mobile

