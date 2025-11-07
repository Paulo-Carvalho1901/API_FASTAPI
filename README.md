# FastAPI APIs Modernas e Assíncronas com Python  
## Curso pela Udemy

🎓 **Aluno:** Paulo Carvalho  
📅 **Data de início:** 2025-11-06  
📌 **Repositório:** `API-FASTAPI`  

---

## 1. Sobre o curso  
Este curso aborda a criação de APIs modernas e assíncronas em Python usando FastAPI.  
Ele inclui:  
- Arquitetura de APIs REST e GraphQL.  
- Uso de programação assíncrona (`async`/`await`) em Python.  
- Integração com bancos de dados, autenticação, deploy e boas práticas.  
- Exemplos reais e hands-on para você aplicar no mundo real.

---

## 2. Principais tópicos / o que aprendi  
- Introdução à FastAPI: rotas, path params, query params, request/response modelos.  
- Programação assíncrona: vantagens, `async`/`await`, uso de `Starlette` sob o capô.  
- Validação de dados com Pydantic.  
- Autenticação e autorização (JWT, OAuth2).  
- Integração com banco de dados (relacional e/ou NoSQL).  
- Deploy da API (ex: Uvicorn, gunicorn, Docker, AWS/GCP).  
- Documentação automática (Swagger UI, Redoc).  
- Testes, tratamento de erros, versionamento de API, performance.

---

## 3. Projeto de exemplo  
Durante o curso, desenvolvi um projeto prático:  
- **Nome do projeto:** `nome-do-projeto`  
- Objetivo: Construir uma API REST completa para gerir “recursos x/y/z”.  
- Tecnologias usadas: FastAPI, Pydantic, SQLAlchemy (ou outro ORM), PostgreSQL (ou outro banco), Docker, etc.  
- Funcionalidades implementadas: criação, leitura, atualização, exclusão (CRUD); autenticação de usuários; documentação automática; testes básicos; deploy simples.

---

## 4. Como rodar localmente  
```bash
# clonar o repositório
git clone https://github.com/SeuUsuario/nome-do-projeto.git  
cd nome-do-projeto  

# instalar dependências (por exemplo em venv)
python -m venv venv  
source venv/bin/activate  # ou venv\Scripts\activate no Windows  
pip install -r requirements.txt  

# configurar variáveis de ambiente
cp .env.example .env  
# editar .env com dados do banco, JWT_SECRET, etc

# iniciar a API
uvicorn app.main:app --reload  
