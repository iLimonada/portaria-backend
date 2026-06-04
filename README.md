# Portaria Inteligente - Backend API 🐍🏢

API RESTful robusta desenvolvida para o gerenciamento de portaria residencial e persistência de dados de moradores, servindo como motor de dados para o aplicativo mobile correspondente.

---

## 🚀 Funcionalidades

- **Endpoints REST:** Rotas otimizadas para criação (`POST`), listagem (`GET`) e exclusão (`DELETE`) de moradores.
- **Persistência Relacional:** Integração total com banco de dados para manutenção estável dos registros.
- **Documentação Automática:** Interface interativa integrada para testes rápidos das rotas.

---

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem base focada em legibilidade e performance.
- **FastAPI:** Framework moderno e de alta performance para construção de APIs.
- **SQLAlchemy (ORM):** Mapeamento objeto-relacional para isolamento da camada de banco de dados.
- **SQLite:** Banco de dados relacional leve e ágil para persistência local (`sql_app.db`).
- **Uvicorn:** Servidor ASGI rápido para produção e desenvolvimento local.

---

## 🔧 Como Executar Localmente

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado na sua máquina.

### 2. Configuração do Ambiente Virtual

Navegue até a pasta do projeto, crie e ative seu ambiente virtual (VENV):

```bash
cd portaria-backend

# No Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate
```

### 3. Instalação das Dependências

Instale todos os pacotes necessários a partir do arquivo de requerimentos gerado pelo `pip freeze`:

```bash
pip install -r requirements.txt
```

### 4. Inicialização do Servidor

Execute o Uvicorn apontando para a sua rede local para permitir conexões externas (como as do aplicativo mobile):

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Acessando a Documentação

Após iniciar o servidor, acesse a documentação automática da API:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🔗 Repositório do Frontend
Confira o código-fonte do aplicativo React Native integrado a este ecossistema em: 
[https://github.com/iLimonada/portaria-frontend](https://github.com/iLimonada/portaria-frontend)
