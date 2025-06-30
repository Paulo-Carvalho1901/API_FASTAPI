from fastapi import FastAPI


# Estanciando o Objeto 
app = FastAPI()


# Criando endpoint (criando as ROTAS)
@app.get('/')
# Criando função raiz
async def raiz():
    return {'msg': 'Curso de Fastapi completo!'}

