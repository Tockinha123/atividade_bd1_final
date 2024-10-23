# 🏥 Sistema de Gestão de Clínicas Médicas

Este repositório contém uma aplicação para gestão de clínicas médicas, desenvolvida com **FastAPI**,**SQLAlchemy** e **Pydantic**, utilizando **PostgreSQL** como banco de dados. O sistema permite gerenciar clínicas, funcionários e suas associações, com controle detalhado e operações CRUD completas.

## ✨ Funcionalidades Principais
- **Clínicas**: CRUD completo para gerenciar clínicas médicas.
- **Funcionários**: CRUD completo para gerenciar médicos e recepcionistas.
- **Associações**: Relacionamento muitos-para-muitos entre clínicas e funcionários.

## 🛠 Tecnologias Utilizadas
- **FastAPI**: Framework para construção de APIs em Python.
- **SQLAlchemy**: ORM utilizado para interagir com o banco de dados.
- **Pydantic**: Realizado para validação dos dados de entrada e saída.
- **PostgreSQL**: Banco de dados relacional.
- **Poetry**: Gerenciamento de dependências.

## 📂 Estrutura do Projeto
- **models/**: Definições das tabelas e relacionamentos.
- **schemas/**: Validações e representações de entrada/saída de dados.
- **routers/**: Implementação dos endpoints da API.
- **database.py**: Configurações do banco de dados.
- **main.py**: Arquivo principal que inicializa a aplicação.

## ⚙️ Como Configurar e Executar o Projeto

### Pré-requisitos
- Python 3.10+
- PostgreSQL instalado
- [Poetry](https://python-poetry.org/)

### Passos para Execução
1. Clone o repositório:
    ```bash
    git clone https://github.com/Tockinha123/atividade_bd1_final
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd atividade_bd1_final
    ```
3. Instale as dependências do projeto:
    ```bash
    poetry install
    ```
4. Crie e configure as variáveis de ambiente (URL do banco de dados) no arquivo `.env`.

5. Execute a aplicação FastAPI:
    ```bash
    task run
    ```
6. Acesse a documentação da API:
    - Acesse `http://127.0.0.1:8000/docs` para usar a interface do Swagger.

**OBS**: O banco está sendo rodado localmente, pois acabaram os créditos na AWS. Dessa forma os scripts de criações de tabelas estão disponibilizados neste repositório, dessa forma é possível rodar o projeto localmente, é necessário criar um BD localmente e executar o script em qualquer software de administração de Banco de Dados da sua escolha (pgAdmin, Beekeeper, DataGrip). O nome do arquivo é -> *script-modelo-lógico.sql*.

## 🔗 Endpoints Importantes

### Clínicas
- **GET /listar_clinicas**: Retorna todas as clínicas cadastradas.
- **GET /buscar_clinica/{cnpj}**: Retorna detalhes de uma clínica específica.
- **POST /criar_clinica**: Adiciona uma nova clínica.
- **PUT /atualizar_clinica/{cnpj}**: Atualiza os dados de uma clínica.
- **DELETE /deletar_clinica/{cnpj}**: Remove uma clínica.

### Funcionários
- **GET /listar_funcionarios**: Lista todos os funcionários cadastrados.
- **GET /buscar_funcionario/{cpf}**: Retorna detalhes de um funcionário.
- **POST /criar_funcionario**: Adiciona um novo funcionário.
- **PUT /atualizar_funcionario/{cpf}**: Atualiza informações de um funcionário.
- **DELETE /deletar_funcionario/{cpf}**: Remove um funcionário.

### Relacionamento Clínicas-Funcionários
- **POST /criar_relacao**: Cria uma relação entre clínica e funcionário.
- **GET /listar_relacoes**: Lista todas as relações clínicas-funcionários.
- **GET /buscar_funcionarios_de_clinica/{cnpj}**: Busca funcionários de uma clínica específica.
- **GET /buscar_clinicas_de_funcionario/{cpf}**: Busca clínicas associadas a um funcionário.
- **PUT /atualizar_relacao/{cnpj}/{cpf}**: Remove a relação entre clínica e funcionário.
- **DELETE /remover_relacao/{cnpj}/{cpf}**: Remove a relação entre clínica e funcionário.

## 📝 Licença
Este projeto está licenciado sob a licença MIT.
