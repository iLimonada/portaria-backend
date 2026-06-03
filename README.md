# AppPortaria 🏢

Sistema completo de controle de portaria residencial desenvolvido para simplificar o gerenciamento de moradores e acessos. O projeto conta com um aplicativo mobile moderno conectado a uma API REST robusta e veloz.

---

## 🛠️ Tecnologias Utilizadas

### Frontend (Mobile)

- **React Native / Expo** — Interface móvel fluida e multiplataforma.
- **TypeScript** — Tipagem estática para maior segurança e manutenção do código.

### Backend (API)

- **Python** — Linguagem principal da aplicação.
- **FastAPI** — Framework moderno e de alto desempenho para APIs.
- **SQLAlchemy** — ORM para mapeamento e manipulação do banco de dados.
- **Pydantic** — Validação de dados e tipagem com schemas estruturados.
- **SQLite** — Banco de dados relacional leve e integrado.

---

## 📐 Estrutura do Projeto

O repositório está organizado em formato **Monorepo**, facilitando a manutenção e evolução do sistema.

```text
├── AppPortaria/        # Aplicativo Mobile (React Native / Expo)
└── portaria-backend/   # API REST (FastAPI / Python)
```

---

## 🚀 Como Executar o Projeto

### 1. Executando o Backend

Acesse a pasta do servidor e configure o ambiente de desenvolvimento:

```bash
cd portaria-backend

source venv/Scripts/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### 2. Executando o Frontend

Abra um novo terminal na raiz do projeto e execute o aplicativo:

```bash
cd AppPortaria

npm install

npx expo start
```

---

## 📱 Recomendação

Utilize o aplicativo **Expo Go** no seu celular para escanear o QR Code gerado pelo Expo e testar a aplicação diretamente em um dispositivo físico.

---
