# Sistema de Cadastro de Usuários

Este é um projeto simples desenvolvido com **FastAPI**, **SQLAlchemy** e **Pydantic** para cadastro de usuários. O principal objetivo do projeto é demonstrar como utilizar a biblioteca **Pydantic** para validação de dados e integrar essa validação com o banco de dados **SQLite** para armazenar as informações dos usuários, como nome, e-mail e idade.

## Tecnologias Utilizadas

- **FastAPI**: Framework para criar APIs de forma rápida e eficiente.
- **SQLAlchemy**: ORM para interagir com o banco de dados SQLite.
- **SQLite**: Banco de dados local para armazenar os dados.
- **Pydantic**: Biblioteca para validação de dados e criação de esquemas (schemas) de forma eficiente e robusta.

## Funcionalidades

1. **Cadastro de Usuários**: A API permite criar um novo usuário, fornecendo nome, e-mail e idade. A biblioteca **Pydantic** é utilizada para validar as entradas de dados.
2. **Listagem de Usuários**: A API lista todos os usuários cadastrados no banco de dados.

## Início rápido
```
pip install -r requirements.txt
uvicorn main:app --reload
```
