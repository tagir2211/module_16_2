from typing import Union

from fastapi import FastAPI, Path

from typing import Annotated


app = FastAPI()

@app.get("/")
async def root_() -> dict:
    return {"message": "Главная страница."}

@app.get("/user/admin")
async def root()-> dict:
    return {"message": "Вы вошли как админ."}

@app.get("/user/{username}/{age}")
async def info_user(username: Annotated[str, Path(min_lenght = 5,
                                                 max_lenght = 20,
                                                 description = 'Enter username',
                                                 example = 'Urban')],
                    age: Annotated[int, Path(ge = 18,
                                             le = 120,
                                             description = 'Enter age',
                                             example = 18)]
                    )-> dict:
    return {"message": f'информация о пользователе. Имя - {username}. Возраст - {age}'}

@app.get("/user/{user_id}")
async def read_user_id(user_id: Annotated[int, Path(ge=1,
                                                    le=100,
                                                    description = 'Enter User ID',
                                                    example = '1')]
                      ) -> dict:
    return {"message": f'Вы вошли как пользователь {user_id}'}