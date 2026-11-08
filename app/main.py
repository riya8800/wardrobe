from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from app.models import Category

app = FastAPI(title="Wardrobe API")

# Hard-coded for now; Phase 3 moves this into PostgreSQL
CATEGORIES = [
    Category(id=1, name="Tops", types=["tank", "tube", "normal"]),
    Category(id=2, name="Dresses", types=["frock"]),
    Category(id=3, name="Skirts", types=["mini", "long"]),
    Category(id=4, name="Shorts", types=["denim", "cotton"]),
]


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).parent.parent / "static" / "index.html")


@app.get("/categories", response_model=list[Category])
def list_categories(name: str | None = None):
    if name:
        return [c for c in CATEGORIES if name.lower() in c.name.lower()]
    return CATEGORIES


@app.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int):
    for c in CATEGORIES:
        if c.id == category_id:
            return c
    raise HTTPException(status_code=404, detail="Category not found")