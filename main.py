from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Aarhus Pubcrawl")
templates = Jinja2Templates(directory="templates")

PUBCRAWL_STOPS = [
    {
        "name": "Mig & Ølsnedkeren",
        "address": "Mejlgade 12, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Mig%20%26%20%C3%98lsnedkeren%20Mejlgade%2012%2C%208000%20Aarhus%20C",
        "rule": "Start stille: kun øl/cider her (ingen shots).",
    },
    {
        "name": "Ris Ras Filliongongong",
        "address": "Mejlgade 24, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Ris%20Ras%20Filliongongong%20Mejlgade%2024%2C%208000%20Aarhus%20C",
        "rule": "Hvis du stiller din øl på bordet inden du er færdig, skal du købe en ny.",
    },
    {
        "name": "Le Coq (Lecoq)",
        "address": "Graven 14, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Le%20Coq%20Graven%2014%2C%208000%20Aarhus%20C",
        "rule": "Cocktail-terning: Èn i gruppen vælger for alle.",
    },
    {
        "name": "Café Under Masken",
        "address": "Bispegade 1, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Caf%C3%A9%20Under%20Masken%20Bispegade%201%2C%208000%20Aarhus%20C",
        "rule": "Ingen telefoner ved bordet i 10 min.",
    },
    {
        "name": "Tir na nÓg",
        "address": "Frederiksgade 38–42, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Tir%20na%20n%C3%93g%20Frederiksgade%2038-42%2C%208000%20Aarhus%20C",
        "rule": "Skål med nabobordet (høfligt!) før I går videre.",
    },
    {
        "name": "Sherlock Holmes Pub",
        "address": "Frederiksgade 76A, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Sherlock%20Holmes%20Pub%20Frederiksgade%2076A%2C%208000%20Aarhus%20C",
        "rule": "Ingen siger et ord før de har drukket en genstand.",
    },
    {
        "name": "Herr Bartels",
        "address": "Åboulevarden 46, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Herr%20Bartels%20%C3%85boulevarden%2046%2C%208000%20Aarhus%20C",
        "rule": "Alle skal have en sidevogn.",
    },
]

def stops_with_numbers():
    return [{"stop_number": i + 1, **stop} for i, stop in enumerate(PUBCRAWL_STOPS)]

@app.get("/api/pubcrawl")
def get_pubcrawl():
    return {"city": "Aarhus C", "stops": stops_with_numbers()}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": {"city": "Aarhus C", "stops": stops_with_numbers()}},
    )
