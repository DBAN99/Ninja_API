from typing import List
from ninja import NinjaAPI, Query
from ninja import Schema, Path
from datetime import date
from pydantic import Field

api = NinjaAPI()


@api.get("/items/{item_id}")
def read_item(request, item_id : int):
    return {"item_id": item_id}

# ------------------------------------------------------
class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return date(self.year, self.month, self.day)

@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}
# ------------------------------------------------------


weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]

@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons[offset: offset + limit]

@api.get("/weapons/search")
def search_weapons(request, q: str, offset: int = 0):
    results = [w for w in weapons if q in w.lower()]
    print(q, results)
    return results[offset: offset + 10]

# ------------------------------------------------------

@api.get("/example")
def example(request, s: str = None, b: bool = None, d: date = None, i: int = None):
    return [s, b, d, i]

# ------------------------------------------------------

class Filters(Schema):
    limit: int = 100
    offset: int = None
    query: str = None
    category__in: List[str] = Field(None, alias="categories")


@api.get("/filter")
def events(request, filters: Filters = Query(...)):
    return {"filters": filters.dict()}

# ------------------------------------------------------

class Item(Schema):
    name: str
    description: str = None
    price: float
    quantity: int


@api.post("/items")
def create(request, item: Item):
    return item

@api.post("/items/{item_id}")
def update(request, item_id: int, item: Item, q: str):
    return {"item_id": item_id, "item": item.dict(), "q": q}