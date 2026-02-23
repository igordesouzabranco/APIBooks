# APIBooks

Esta é uma API REST simples que permite a manipulação de dados de livros. A API foi construída com Flask, Marshmallow e SQLAlchemy, e é ideal para gerenciar uma coleção de livros em um banco de dados relacional.

## Funcionalidades
- **Criar um livro**
- **Listar todos os livros**
- **Obter detalhes de um livro específico**
- **Atualizar os dados de um livro**
- **Excluir um livro**

## Tecnologias Utilizadas
- **Flask**: Um microframework para Python que facilita a criação de APIs.
- **Marshmallow**: Uma biblioteca para serialização/deserialização de objetos complexos, permitindo a transformação entre tipos de dados complexos e tipos de dados nativos do Python.
- **SQLAlchemy**: Um ORM (Object Relational Mapper) para facilitar a interação com bancos de dados.

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/igordesouzabranco/APIBooks.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd APIBooks
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
- Para iniciar a API:
  ```bash
  python app.py
  ```
- A API estará disponível em `http://localhost:5000`.

## Endpoints
| Método | Endpoint                | Descrição                      |
|--------|-------------------------|-------------------------------|
| POST   | /livros                 | Cria um novo livro            |
| GET    | /livros                 | Lista todos os livros         |
| GET    | /livros/{id}           | Obtém um livro pelo id         |
| PUT    | /livros/{id}           | Atualiza um livro             |
| DELETE | /livros/{id}           | Exclui um livro               |

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou um Pull Request.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
