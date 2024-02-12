#FROM arquivos ou bibliotecas IMPORT classes, variaveis
from fastapi import FastAPI
from typing import List
# from pydantic import BaseModel
from models import User, Role
from uuid import UUID, uuid4

#Passando a aplicação dentro de uma variável
app = FastAPI()

#criando uma lista
db: List[User] = [
    User(
        id=uuid4(),
        first_name='Ana',
        last_name='Maria',
        email='email@gmail.com',
        role=[Role.role_1]
    ),
    User(
        id=uuid4(),
        first_name='Cynthia',
        last_name='Zanona',
        email='email@gmail.com',
        role=[Role.role_2]
    ),
    User(
        id=uuid4(),
        first_name='Camila',
        last_name='Silva',
        email='email@gmail.com',
        role=[Role.role_3]
    )
]

#APRENDENDO UM CRUD
@app.get('/')
async def root():
    return {"message": "Hello, world"}




# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None 

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, busca: Union[str, int] = None):
#     return {"item_id": item_id, "busca": busca}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "Item_id": item_id}