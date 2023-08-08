from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
def get_greeting():
    return 'Hello!'

@app.get('/calculator')
def calculator(a: int, b: int, operation: str):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'
