from fastapi import FastAPI, Query, Header
from typing import Annotated
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# @app.get("/sample")
# def  read_root():
#     return {"message": "FastAPI"}

# @app.get("/items/{item_id}/detail")
# def read_item(item_id):
#     return {"item_id": item_id, "item_name": "Tシャツ"}

# items = [
#     "Tシャツ",
#     "スカート",
#     "ブーツ",
#     "コート"
#         ]

# @app.get("/items")
# def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
#     return {"items": items[skip : skip + limit]}

# class Item(BaseModel):
#     name: str
#     price: float
#     description: Union[str, None] = None

# @app.post("/items/")
# def create_item(item: Item):
#     print(f"データを登録します: {item.name}, {item.price}, {item.description}")
#     return item

@app.get("/sample")
def read_sample(authorization: Union[str, None] = Header(default=None)):
    print(authorization)
    return {"message": "ヘッダー情報を取得しました"}
