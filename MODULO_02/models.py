"""Optional indica que um atributo pode ter valor ou não (pode ser None)"""
from typing import Optional # Notação de tipos


"""Quando criamos uma classe herdando dela, ganhamos automaticamente validação de dados"""
from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
