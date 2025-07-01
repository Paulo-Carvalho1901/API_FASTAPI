from fastapi import FastAPI



# Estanciando o Objeto 
app = FastAPI()


# Criando endpoint (criando as ROTAS)
@app.get('/mensagem')
# Criando função raiz
async def mensagem():
    return {'msg': 'Curso de Fastapi completo!'}


# Chamando a execução da aplicação "uvicorn main:app"
# http://127.0.0.1:8000 o mesmo -> http://localhost:8000


# Criando entrada para execução da aplicação
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, 
                log_level='info', reload=True)