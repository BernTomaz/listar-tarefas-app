# Listar Tarefas App

Este projeto é uma aplicação simples de gerenciamento de tarefas construída com Flask e Python. A aplicação permite criar, listar, atualizar e deletar tarefas, armazenando os dados localmente em um arquivo chamado `memory`.

## Estrutura do Projeto


```
listar-tarefas-app  
├── .venv/               # Ambiente virtual do projeto  
├── src/  
│   ├── __pycache__/     # Cache de bytecode compilado do Python  
│   ├── app.py           # Ponto de entrada da aplicação Flask  
│   ├── crud.py          # Operações CRUD para gerenciamento de tarefas  
│   ├── database.py      # Configurações e conexões com o banco de dados  
│   ├── main.py          # Arquivo principal para execução da aplicação  
│   ├── memory/          # Diretório para armazenamento local  
│   ├── models.py        # Definição dos modelos de dados  
│   └── schemas.py       # Schemas para validação e serialização de dados  
├── README.md            # Documentação do projeto  
└── requirements.txt     # Lista de dependências do projeto  
```


## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu_usuario/listar-tarefas-app.git 
   cd listar-tarefas-app    
   ```


2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv source venv/bin/activate # Para Linux/Mac 
   venv\Scripts\activate # Para Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```


## Uso

Para iniciar a aplicação, execute o seguinte comando:


```
python app.py
```


A aplicação estará disponível em `http://127.0.0.1:5000`.

## Endpoints

- `POST /tasks`: Cria uma nova tarefa.
- `GET /tasks`: Lista todas as tarefas.
- `GET /tasks/{task_id}`: Obtém uma tarefa pelo ID.
- `PUT /tasks/{task_id}`: Atualiza uma tarefa pelo ID.
- `DELETE /tasks/{task_id}`: Deleta uma tarefa pelo ID.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.