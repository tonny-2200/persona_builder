# main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from reddit_persona import generate_persona, extract_username
import markdown
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "persona": None})

import os
from datetime import datetime

@app.post("/", response_class=HTMLResponse)
async def get_persona(request: Request, profile_url: str = Form(...)):
    try:
        raw_persona = generate_persona(profile_url)
        html_persona = markdown.markdown(
            raw_persona,
            extensions=["markdown.extensions.extra", "markdown.extensions.nl2br"]
        )


        # ✅ Save raw persona to .txt file
        username = extract_username(profile_url)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"persona_{username}_{timestamp}.txt"
        output_path = os.path.join("personas", filename)

        # Create folder if it doesn't exist
        os.makedirs("personas", exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(raw_persona)

    except Exception as e:
        html_persona = f"<b>Error generating persona:</b> {e}"

    return templates.TemplateResponse("index.html", {"request": request, "persona": html_persona})



if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
