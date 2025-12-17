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
        "name": "Bodegaen",
        "address": "Åboulevarden 39, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/place/Willi's/@56.1565188,10.2057896,617m/data=!3m2!1e3!4b1!4m6!3m5!1s0x464c3f70a9e4e737:0x3fc6d503e66c21be!8m2!3d56.1565188!4d10.2073005!16s%2Fg%2F11qc0bv6s9?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D",
        "rule": "Alle skal have en sidevogn.",
    },
    {
        "name": "Bodegaen",
        "address": "Åboulevarden 33, 8000 Aarhus C",
        "maps_url": "https://www.google.com/maps/place/Bodegaen/@56.1558507,10.2086985,617m/data=!3m2!1e3!4b1!4m6!3m5!1s0x464c3f913ee136db:0xe5868952cc804806!8m2!3d56.1558507!4d10.2086985!16s%2Fg%2F1q5ccd4_0?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D",
        "rule": "Alle skal have en sidevogn.",
    },


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
