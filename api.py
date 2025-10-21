from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {
        "Dark Souls": {
            "Fecha de lanzamiento": 2011,
            "Plataformas": ["PC", "PS3", "XBOX360"]
        },
        "Dark Souls 2": {
            "Fecha de lanzamiento": 2014,
            "Plataformas": ["PC", "XBOX360", "XBOX ONE", "PS3", "PS4"]
        },
        "Dark Souls 3": {
            "Fecha de lanzamiento": 2016,
            "Plataformas": ["PS4", "PC", "XBOX ONE"]
        }
    }
