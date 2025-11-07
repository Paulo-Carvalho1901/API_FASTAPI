from typing import Optional # Notação de tipos

from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
