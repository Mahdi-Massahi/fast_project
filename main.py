
from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
def greeting():
    return 'Hello!'

@app.get('/sum/{num1}/{num2}')
def calculate_sum(num1: int, num2: int):
    return {'result': num1 + num2}


