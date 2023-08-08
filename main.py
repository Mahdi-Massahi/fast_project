from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting')
def get_greeting():
    return 'Hello!'
