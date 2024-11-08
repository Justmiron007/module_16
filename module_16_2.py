from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(gt=1, le=100, description="Enter User ID")]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
