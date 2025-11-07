from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'Message': "Hello World"}


@app.get('/about')
def about():
    return{'Message':'Shaon who always try to learn'}