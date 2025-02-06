# Listar Tarefas App

Este projeto é uma aplicação simples de gerenciamento de tarefas construída com FastAPI e Python. A aplicação permite criar, listar e deletar tarefas, armazenando os dados localmente em um arquivo chamado `memory`.

## Estrutura do Projeto

```
listar-tarefas-app
├── src
│   ├── main.py          # Ponto de entrada da aplicação FastAPI
│   ├── models.py        # Definição do modelo de dados para tarefas
│   ├── schemas.py       # Schemas Pydantic para validação de dados
│   ├── crud.py          # Operações CRUD para gerenciamento de tarefas
│   └── database.py      # Mecanismo de armazenamento local
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── .gitignore            # Arquivos e diretórios a serem ignorados pelo Git
```

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu_usuario/listar-tarefas-app.git
   cd listar-tarefas-app
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar a aplicação, execute o seguinte comando:

```
uvicorn src.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Endpoints

- `POST /tasks`: Cria uma nova tarefa.
- `GET /tasks`: Lista todas as tarefas.
- `DELETE /tasks/{task_id}`: Deleta uma tarefa pelo ID.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.