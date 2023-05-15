from typing import List, Optional

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

_BOOKS = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BookItem(BaseModel):
    title: str
    review: Optional[str] = None


@app.post("/books/{username}")
async def add_book(username: str, book_item: BookItem):
    if username not in _BOOKS:
        _BOOKS[username] = []
    _BOOKS[username].append(book_item.dict())
    return {"status": "OK"}


@app.get("/books/{username}", response_model=List[BookItem])
async def get_books(username: str):
    return _BOOKS.get(username, [])


@app.delete("/books/{username}")
async def delete_book(username: str, book_index: int):
    try:
        _BOOKS.get(username).pop(book_index)
        return {"status": "OK"}
    except (AttributeError, IndexError):
        return {"status": "book not found"}


@app.put("/books/{username}/{book_title}")
async def update_book(username: str, book_title: str, review: Optional[str] = None):
    if username in _BOOKS:
        for book in _BOOKS[username]:
            if book["title"] == book_title:
                book["review"] = review
                return {"status": "OK"}
    return {"status": "Book not found"}


@app.get("/logo.png")
async def plugin_logo():
    filename = "logo.png"
    return FileResponse(filename, media_type="image/png")


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, media_type="application/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
        return Response(text, media_type="text/yaml")
