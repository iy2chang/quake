from fastapi import FastAPI

app = FastAPI()


QUAKES = [
    {"mag": 4.5, "place": "2 km N of Honchō, Japan", "depth": 90, "time": "2026-10-21T01:04:29Z"},
    {"mag": 4.7, "place": "33 km NE of Shizunai-furukawachō, Japan", "depth": 94, "time": "2026-10-21T14:40:50Z"},
    {"mag": 4.3, "place": "19 km S of Makurazaki, Japan", "depth": 169, "time": "2026-10-21T15:13:07Z"},
    {"mag": 5.3, "place": "0 km NNE of Yōkaichiba, Japan", "depth": 42, "time": "2026-10-01T12:27:11Z"},
    {"mag": 4.9, "place": "3 km WSW of Shibayama, Japan", "depth": 73, "time": "2026-10-07T19:13:50Z"},
]

@app.get("/")
def home():
    return {"message": "Hello from my earthquake API"}

@app.get("/quakes")
def get_quakes():
    return QUAKES

@app.get("/count")
def get_count():
    return {"count": len(QUAKES)}