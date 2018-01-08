# Landing Django

Um criador de landing-pages feito em Django 2.1

* [LIVE DEMO](https://landing-django.herokuapp.com/)

## Getting Started

As instruções a seguir vai ajudá-los a baixar e ter uma cópia do projeto em sua máquina local para prosseguir com o desenvolvimento.

### Pré-requisitos

Algumas tecnologias que você vai precisar ter instalada em seu SO antecipadamente são:

```
Python 3.x+ 
Pip (Qualquer versão)
PostgreSQL 9.x+
```

Criaremos o nosso BD a seguir:

```
#Para ir direto ao prompt do postgres
$ sudo -u postgres psql

postgres=# CREATE DATABASE landing;
CREATE DATABASE
#Por padrão o PostgreSQL usa um sistema de autenticação chamado Peer Authentication para conexões locais, isso significa que se o nome do usuário do SO corresponder a um nome de usuário válido no postgres, esse usuário poderá efetuar login sem autenticação adicional.
postgres=# CREATE USER clinic WITH PASSWORD 'passwd';
CREATE ROLE
#Dar todas as permissões do banco para o meu usuário
postgres=# GRANT ALL PRIVILEGES ON DATABASE landing TO clinic;
GRANT
```
Abaixo um tutorial redigido por mim para apresentar como provisionar PostgreSQL corretamente: 
* [PostgreSQL](https://github.com/Projet0sDjango/pyMentors/wiki/Provisionando-PostgreSQL)

### Instalando

A seguir, passo-a-passo de como baixar, instalar e rodá-lo.

```
$ mkdir /workspace && cd /workspace
# Ou qualquer outro caminho que você armazene seus projetos

# Realizando o download do projeto
$ git clone git@github.com:rafaelribeiroo/landing-django.git

# Acessar projeto pelo terminal
$ cd landing-django

# No python 3.x ele tem uma ferramenta de isolar ambientes nativa similar ao VirtualEnv
$ python -m venv .venv

# Ativando o ambiente virtual
$ source .venv/bin/activate

# Instalando as dependências
$ pip install -r requirements.txt 

# Realizando as migrações do banco de dados
$ make migrations
$ make migrate

# Criando o usuário para acessar o CMS
$ make user
> Defina um user de sua preferência: clinic
> Um e-mail fictício: admin@admin.com
> senha: passwd
```

### Django Admin

Para acessar o CMS, use as credenciais abaixo:

```
Usuário: clinic
Senha: passwd
```

### Variáveis de Ambiente

Vá na raíz do projeto e execute o arquivo secret_key.py

```
$ python secret_key.py
```

No arquivo .env_exemplo, renomeie-o para .env e deixe conforme abaixo:

```
SECRET_KEY=COLE_AQUI_O_RESULTADO_DA_EXECUCAO_DO_SCRIPT
DEBUG=TRUE
DB_NAME=landing
DB_USER=clinic
DB_PASSWORD=passwd
DB_HOST=localhost
```

### Tudo Pronto!

```
$ make run
```


## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details