from fastapi import FastAPI


app = FastAPI() # instanciando FastAPI

# criado banco em memória
curso = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "titulo": "algoritimo logica de programação",
        "aulas": 87,
        "horas": 67
    }
}


# Criando o primeiro endpoint GET
@app.get('/cursos')
# Funções assíncronas são úteis para lidar com operações que podem demorar (como acesso a banco de dados).
async def get_cursos():
    return curso

# Criando chamada de execução
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
