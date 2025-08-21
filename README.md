# Data Mesh POC

Este projeto é uma prova de conceito (POC) para um sistema de Data Mesh utilizando FastAPI, autenticação JWT e templates Jinja2.

## Funcionalidades
- Autenticação de usuários
- Dashboard com visualização de domínios de dados
- Upload e visualização de arquivos CSV
- Gerenciamento de usuários

## Estrutura do Projeto

```
├── app/
│   ├── main.py          # Ponto de entrada da aplicação FastAPI
│   ├── auth.py          # Lógica de autenticação e geração de tokens JWT
│   ├── users.py         # Gerenciamento de usuários
│   ├── users.json       # Base de dados simulada de usuários
│   ├── domains/         # Domínios de negócio
│   ├── static/          # Arquivos estáticos (CSS, JS, imagens)
│   └── templates/       # Templates HTML (Jinja2)
├── data/
│   ├── clientes.csv     # Exemplo de dados de clientes
│   └── produtos.csv     # Exemplo de dados de produtos
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

## Pré-requisitos
- Python 3.10+
- pip

## Instalação
1. Clone o repositório:
	```cmd
	git clone https://github.com/yanhkawakami/data-mesh-poc.git
	cd data-mesh-poc
	```
2. Instale as dependências:
	```cmd
	pip install -r requirements.txt
	```

## Executando o Projeto
1. Execute o servidor FastAPI com Uvicorn:
	```cmd
	uvicorn app.main:app --reload
	```
2. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## Usuários de Teste
O arquivo `app/users.json` contém usuários de exemplo. Você pode editar ou adicionar novos usuários conforme necessário.

## Estrutura dos Dados
Os arquivos CSV em `data/` representam domínios de dados que podem ser visualizados no dashboard.

## Personalização
- Para adicionar novos domínios, coloque arquivos CSV em `data/`.
- Para modificar templates, edite os arquivos em `app/templates/`.

## Licença
Este projeto é apenas para fins educacionais e de demonstração.
