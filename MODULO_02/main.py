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

