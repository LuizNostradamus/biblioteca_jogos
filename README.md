# Biblioteca de Jogos

Aplicação web simples para cadastrar os jogos que você joga (título, plataforma, gênero, status, nota e preço), feita com **Python**, **Streamlit** e **MySQL**.

## Funcionalidades

- Formulário de cadastro de jogos
- Plataformas: PS5, Xbox, Switch, PC e Mobile
- Gêneros: Ação, Aventura, RPG, FPS, Battle Royale, MOBA, Estratégia, Simulação, Esporte, Corrida, Luta, Plataforma, Terror, Puzzle, Mundo aberto, Roguelike, Indie e Outro
- Status do jogo: Jogando, Terminado ou Abandonado
- Nota de 0 a 10 (de 0,5 em 0,5)
- Os dados são salvos na tabela `jogos` do MySQL

## Tecnologias

- Python 3
- [Streamlit](https://streamlit.io/) (interface web)
- MySQL (banco de dados)
- mysql-connector-python (conexão Python com o MySQL)
- pandas (importado em `banco.py`)

## Estrutura do projeto

```
biblioteca_jogos/
├── app.py                # Interface do Streamlit (formulário)
├── banco.py              # Conexão e funções do banco de dados
├── biblioteca_jogos.sql  # Script de criação do banco, tabela e usuário
└── README.md
```

## Como executar

### 1. Pré-requisitos

- Python 3 instalado
- MySQL Server instalado e em execução

### 2. Criar o banco de dados

Abra o MySQL (Workbench ou terminal) e execute o conteúdo do arquivo `biblioteca_jogos.sql`. Ele cria:

- o banco `biblioteca_jogos`
- a tabela `jogos`
- o usuário `desenvolvedor`, com permissão apenas de `SELECT` e `INSERT` na tabela `jogos`

### 3. Instalar as dependências

```
pip install streamlit mysql-connector-python pandas
```

### 4. Rodar a aplicação

Entre na pasta do projeto (onde está o `app.py`) e execute:

```
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

## Configuração

A conexão com o banco está na função `conectar()` do arquivo `banco.py`. Se o seu MySQL usar outro host, usuário, senha ou nome de banco, altere os valores ali. O usuário e a senha usados são os mesmos definidos no script `biblioteca_jogos.sql`.

## Estrutura da tabela `jogos`

| Campo       | Tipo          | Observação                 |
|-------------|---------------|----------------------------|
| id          | INT           | Chave primária, automático |
| titulo      | VARCHAR(50)   | Obrigatório                |
| plataforma  | VARCHAR(20)   | Obrigatório                |
| genero      | VARCHAR(30)   | Obrigatório                |
| status_jogo | VARCHAR(15)   | Obrigatório                |
| nota        | DECIMAL(3,1)  | Opcional, de 0 a 10        |
| preco       | DECIMAL(7,2)  | Opcional                   |

## Problemas comuns

- **`File does not exist: app.py`**: o terminal não está na pasta do projeto. Use `cd` para entrar na pasta antes de rodar o comando.
- **`Not all parameters were used in the SQL statement`**: a quantidade de `%s` no `INSERT` do `banco.py` precisa ser igual à quantidade de colunas e de valores.
- **`INSERT command denied`**: o `INSERT` do `banco.py` precisa apontar para a tabela `jogos`, que é a única em que o usuário tem permissão.

