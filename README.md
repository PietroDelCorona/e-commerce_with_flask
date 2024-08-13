# E-commerce Project with Flask

Bem-vindo ao projeto de e-commerce desenvolvido com Flask! Este projeto demonstra um sistema básico de e-commerce com funcionalidades como validação de e-mail, criação de usuários, gerenciamento de produtos e controle de saldo do cliente.

### Funcionalidades

<ul>
    <li>Criação de Usuários: Registro e autenticação de usuários com gerenciamento de perfil</li>
    <li>Gerenciamento de Produtos: Produtos pré-carregados no sistema, com possibilidade de visualização e filtragem.</li>
    <li>Saldo do Cliente: Controle do saldo disponível de cada cliente para realizar compras.</li>
</ul>

### Tecnologias Utilizadas

<ul>
    <li><strong>Flask:</strong> Framework web em Python.</li>
    <li><strong>SQLAlchemy:</strong> ORM para manipulação do banco de dados.</li>
    <li><strong>Flask-Bcrypt: </strong>Para hashing e verificação de senhas.</li>
    <li><strong>Flask-Login: </strong>Gerenciamento de sessão e autenticação de usuários.</li>
    <li><strong>Flask-WTF: </strong>Validação de formulários.</li>
    <li><strong>Bootstrap: </strong>Framework CSS para estilização.</li>
    <li><strong>Jinja2: </strong>Motor de templates para renderização de HTML.</li>
</ul>

### Estrutura do Projeto

<ul>
    <li>market/models.py: Definições dos modelos de banco de dados.</li>
    <li>market/forms.py: Definições dos formulários.
</li>
    <li>market/routes.py: Definição das rotas e lógica de negócios.</li>
    <li>market/templates/: Diretório contendo os templates Jinja2.</li>
    <li>requirements.txt: Lista de dependências do projeto.</li>
    <li>run.py: Script de inicialização do servidor.</li>
</ul>

### Como Usar

<ol>
    <li>Registrar um novo usuário:</li>
    <ul>
        <li>Acesse a rota /register e preencha o formulário de registro.</li>
    </ul>
    <li>Fazer Login</li>
    <ul>
        <li>Acesse a rota /login e insira suas credenciais para autenticação.</li>
    </ul>
    <li>Visualizar Produtos</li>
    <ul>
        <li>Navegue até a rota /market para ver a lista de produtos disponíveis.</li>
    </ul>
    <li>Gerenciar Saldo</li>
    <ul>
        <li>O saldo do cliente pode ser visualizado na página do perfil após o login.</li>
    </ul>
</ol>

### Contribuindo

Se desejar contribuir com o projeto, siga as seguintes etapas:

<ol>
    <li>Faça um fork do repositório.</li>
    <li>Crie uma branch para sua feature ou correção.</li>
    <li>Faça commit das suas alterações.</li>
    <li>Faça push para a branch</li>
    <li>Abra um pull request.</li>
</ol>