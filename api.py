import uvicorn
from fastapi import FastAPI, Form
from Models.llama import llama_check

app = FastAPI()


@app.post("/check")
def check(url: str = Form(...)):
    path = llama_check(url)
    result = {'URL': path}
    return result

if __name__ == '__main__':
    """ The main """
    uvicorn.run(app, host='localhost', port=8000)