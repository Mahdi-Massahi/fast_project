from fastapi import FastAPI, List

app = FastAPI()

@app.get('/greeting')
async def greeting():
    return {'message': 'Hello!'}

@app.get('/multiply')
async def multiply_numbers(numbers: List[int]):
    multiplied_numbers = [num * 2 for num in numbers]
    return {'multiplied_numbers': multiplied_numbers}

from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
async def greeting():
    return {'message': 'Hello!'}

from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
def greeting():
    return 'Hello!'
from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
def greeting():
    return 'Hello!'

@app.get('/odd_numbers')
def get_odd_numbers(numbers: List[int]):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers
