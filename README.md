# Tela de Login Django

Este é um projeto simples de tela de login desenvolvido com Django. Foi criado com o intuito de colocar em prática os conhecimentos em Django e servir como base para futuros projetos mais complexos.

## Funcionalidades

- Página de login simples.
- Utilização de ambiente virtual (venv).
- Utilização de um arquivo `.env` para a configuração da `SECRET_KEY`.
- Integração com banco de dados através de migrações do Django.
- Criação de usuário administrador para acesso ao painel de administração.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python (3.x recomendado)
- Django
- Ambiente virtual (recomendado para isolamento de dependências)

## Como executar o projeto

Siga os passos abaixo para executar o projeto localmente:

1. Clone este repositório: 
   git clone https://github.com/tdias93/LoginScreen.git

2. Navegue até o diretório do projeto:
   cd seu-projeto

3. Crie e inicialize o ambiente virtual:
   python -m venv venv

4. Ative o ambiente virtual:

- No Windows: venv\Scripts\activate
- No macOS e Linux: source venv/bin/activate

5. Instale as dependências:
   pip install -r requirements.txt

6. Crie um arquivo `.env` na raiz do projeto e adicione a seguinte linha, substituindo `SUA_SECRET_KEY_AQUI` por uma chave secreta:
   SECRET_KEY=SUA_SECRET_KEY_AQUI

7. Execute as migrações do banco de dados:
   python manage.py migrate

8. Crie um superusuário para acessar o painel de administração:
   python manage.py createsuperuser

9. Inicie o servidor de desenvolvimento:
   python manage.py runserver



Agora você pode acessar a tela de login em [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login) e o painel de administração em [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) utilizando as credenciais do superusuário que você criou.

Divirta-se explorando o projeto! Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.

