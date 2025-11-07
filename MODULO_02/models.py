"""
O que é o Pydantic?
Pydantic é uma biblioteca Python usada para:

Validar dados automaticamente
Garantir o tipo correto das informações
Converter valores para o tipo esperado
Criar modelos de dados estruturados

Ele é muito usado em APIs (como com FastAPI) para definir a estrutura 
dos dados que entram e saem da aplicação.

Pydantic funciona baseado em tipagem (type hints do Python).

"""
"""Optional indica que um atributo pode ter valor ou não (pode ser None)"""
from typing import Optional # Notação de tipos


"""Quando criamos uma classe herdando dela, ganhamos automaticamente validação de dados"""
from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
