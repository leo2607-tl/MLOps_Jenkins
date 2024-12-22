from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/version")
def get_version():
    return {"version": "1.0.0"}

class Number(BaseModel):
    value: int

@app.post("/check_prime")
def check_prime(number: Number):
    value = number.value
    if value < 2:
        return {"is_prime": False}
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)