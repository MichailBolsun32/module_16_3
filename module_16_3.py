from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

#Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
users = {'1': 'Имя: Example, возраст: 18'}

#Реализуйте get запрос по маршруту '/users', который возвращает словарь users.

@app.get('/users')
async def get_all_massages() -> dict:
    return users

#Реализуйте post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению ключом значение строки
# "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
#Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.

@app.post('/user/{username}/{age}')
async def create_message(username: Annotated[str, Path(min_length=5,
                                             max_length=20,
                                             description='Enter username',
                                             example='UrbanUser')] ,
                        age: Annotated[int, Path(ge=18,
                                      le=120,
                                      description='Enter age',
                                      example='24'
                                      )]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

#Реализуйте put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку
# "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
#Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.

@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: Annotated[int, Path(ge=1,
                                                      le=150,
                                                      description='Enter user_id',
                                                      example=1)],
                         username: Annotated[str, Path(min_length=5,
                                                       max_length=20,
                                                       description='Enter username',
                                                       example='UrbanUser')],
                         age: Annotated[int, Path(ge=18,
                                                  le=120,
                                                  description='Enter age',
                                                  example='24'
                                                  )]) -> str:
    if f'{user_id}' in users:
        users[f'{user_id}'] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'
    else:
        raise HTTPException(status_code=404, detail=f"Users с {user_id} не найден")

#Реализуйте delete запрос по маршруту '/user/{user_id}',
# который удаляет из словаря users по ключу user_id пару.
#Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.

@app.delete('/user/{user_id}')
async def delete_message(user_id: Annotated[int, Path(ge=1,
                                                      le=150,
                                                      description='Enter user_id',
                                                      example=1)]) -> str:
    if f'{user_id}' in users:
        users.pop(f'{user_id}')
        return f'The user {user_id} is deleted'
    else:
        raise HTTPException(status_code=404, detail=f"Users с {user_id} не найден")