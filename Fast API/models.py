#BaseModel: usa métodos pré-definidos para criar o formato do body da requisição
from pydantic import BaseModel
# cria ids aleatórios 
from uuid import UUID, uuid4
# importa tipos. Aqui estamos importanto Optional, que deixa vc passar o id ou não
from typing import Optional, List
#importando o tipo Enum
from enum import Enum

class Role(str, Enum):
    role_1= 'admin'
    role_2= 'aluna'
    role_3= 'instrutora'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]