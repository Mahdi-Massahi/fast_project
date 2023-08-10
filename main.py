@app.get("/greeting")
def read_root():
    return {"Hello!"}
