from fastapi import FastAPI, List

app = FastAPI()

@app.get('/greeting')
async def greeting():
    return {'message': 'Hello!'}

@app.get('/multiply')
async def multiply_numbers(numbers: List[int]):
    multiplied_numbers = [num * 2 for num in numbers]
    return {'multiplied_numbers': multiplied_numbers}
