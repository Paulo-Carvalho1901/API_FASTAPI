from typing import Optional, List, Any

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path, Query, Header, Depends

from time import sleep

from models import Curso

# Simulando conexão com banco de dados
def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão do banco de daods.')
        sleep(1)

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
async def get_cursos(db: Any = Depends(fake_db)): # Injeção de dependencia
    return cursos


# Criando endpoint GET curso_id
@app.get('/cursos/{curso_id}') # endpoint cursos/curso_id, parâmetro curso_id
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre entre 1 e 2', gt=0, lt=3), db: Any = Depends(fake_db)): # utilizando o parâmetro curso_id e informando que ele é inteiro

    # tratando o erro de keyError
    try:
        curso = cursos[curso_id] # criado variável curso que recebe cursos com o parâmtro curso_id
        return curso # retorno variavel 'curso' que recebe o cursos (banco Fake em memória) atualizado 
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!') # HTTPException tratando as except e os statudos_code


# Criando endpoint POST
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)): # Injeção de dependencia
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


# Criando endpoint PUT
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)): # Injeção de dependencia
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com ID {curso_id}')


# Criando endpoint DELETE
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)): # Injeção de dependencia
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com isso ID {curso_id}')


@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c

    print(f'X-GEEK: {x_geek}')

    return {'Resultado': soma}


# Criando chamada de execução
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
