import httpx
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()



def fetch_quakes(period):
    """Download earthquakes from USGS and simplify them."""
    USGS_URL = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_{period}.geojson"
    response = httpx.get(USGS_URL)
    data = response.json()

    quakes = []
    for feature in data["features"]:
        props = feature["properties"]
        lon, lat, depth = feature["geometry"]["coordinates"]
        quakes.append({
            "mag": props["mag"],
            "place": props["place"],
            "depth": depth,
            "lat": lat,
            "lon": lon,
            "time": datetime.fromtimestamp(props["time"] / 1000, tz=timezone.utc).isoformat(),
        })
    return quakes

@app.get("/")
def home():
    return {"message": "Hello from my earthquake API!"}

@app.get("/quakes")
def get_quakes(min_mag: float = 0, period: str = "week"):
    if period not in ["day", "week", "month"]:
        return {"error": "period must be day, week or month"}
    results = []
    for quake in fetch_quakes(period):
        if 20 <= quake["lat"] <= 46 and 122 <= quake["lon"] <= 153 :    # japan only
            if quake["mag"] is not None and quake["mag"] >= min_mag:
                results.append(quake)
    return results

@app.get("/count")
def get_count():
    return {"count": len(fetch_quakes())}
