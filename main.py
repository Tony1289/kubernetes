from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Replace "templates" with your directory name

@app.get("/")
async def form(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})

@app.post("/")
async def form_post(request: Request, text_input: str = Form(...)):
    # Process the form submission here
    return templates.TemplateResponse('form.html', {'request': request, 'text_input': text_input})

