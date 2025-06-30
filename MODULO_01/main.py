from fastapi import FastAPI


# Estanciando o Objeto 
app = FastAPI()


# Criando endpoint (criando as ROTAS)
@app.get('/')
# Criando função raiz
async def raiz():
    return {'msg': 'Curso de Fastapi completo!'}


# Chamando a execução da aplicação "uvicorn main:app"
# http://127.0.0.1:8000 ou http://localhost:8000
