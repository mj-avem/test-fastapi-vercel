from pydantic import BaseModel
from typing import Optional
from datetime import date

class RecenseadorDto(BaseModel):
    id: Optional[int] = None
    nome: str
    usuario: str
    senha: str
    email: str
    data_nascimento: date
    ativo: bool
