from fastapi import FastAPI

app = FastAPI()


@app.get("/get_datas")
async def root():
    return {
        "code": 200,
        "message": "success",
        "data": {
            "mysql_table_model": {
                "id": 123,
                "username": "root",
                "password": "<PASSWORD>",
            }
        }
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
