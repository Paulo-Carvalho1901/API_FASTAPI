from fastapi import FastAPI, HTTPException, status

from models import Curso


app = FastAPI() # instanciando FastAPI

# criado banco em memória
cursos = {
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
    return cursos


# Criando endpoint GET curso_id
@app.get('/cursos/{curso_id}') # endpoint cursos/curso_id, parâmetro curso_id
async def get_curso(curso_id: int): # utilizando o parâmetro curso_id e informando que ele é inteiro
    # tratando o erro de keyError
    try:
        curso = cursos[curso_id] # criado variável curso que recebe cursos com o parâmtro curso_id
        return curso # retorno variavel 'curso' que recebe o cursos (banco Fake em memória) atualizado 
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!') # HTTPException tratando as except e os statudos_code


# Criando endpoint POST
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


# Criando endpoint PUT
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com ID {curso_id}')

# Criando chamada de execução
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
