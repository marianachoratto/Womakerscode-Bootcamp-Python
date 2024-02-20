#FROM arquivos ou bibliotecas IMPORT classes, variaveis
from fastapi import FastAPI, HTTPException
from typing import List
# from pydantic import BaseModel
from models import User, Role
from uuid import UUID, uuid4

#Passando a aplicação dentro de uma variável
app = FastAPI()

#criando uma lista
db: List[User] = [
    User(
        id=UUID("d09c8620-0b0f-43fc-8a13-cad8cec24df5"),
        first_name='Ana',
        last_name='Maria',
        email='email@gmail.com',
        role=[Role.role_1]
    ),
    User(
        id=UUID("94ddfb97-7f29-493f-bbeb-edfcb60d6723"),
        first_name='Cynthia',
        last_name='Zanona',
        email='email@gmail.com',
        role=[Role.role_2]
    ),
    User(
        id=UUID("9f100acb-0f8a-446a-8af9-af47cd1eb899"),
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

#fazendo um GET. Listagem de todos os alunos
@app.get('/api/users')
async def get_users():
    return db;

#Listando um usuário específico 
@app.get('/api/users/{id}')
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

#Vamos instalar uma extensão que vai servir como cliente. Thunder Client
#Usando POST. OBS: o usuário não vai ser realmente incluído no BD 
@app.post('/api/users')
async def add_usuario(user: User):
    db.append(user)
    return {"id": user.id}

#usa-se o for, pois o código precisa rodar em todos os usuários até achar aquele que eu quero excluir
@app.delete('/api/users/{id}')
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
        #return vazio volta 200
    raise HTTPException(
        status_code = 404,
        detail=f"Usuário com o id {user} não econtrado."
    )

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