from fastapi import FastAPI

app = FastAPI()

lobbies = ['hi there','yellow dog']
players = []
games = []

@app.get("/")
async def root():
    return {"message": "Hello World", "lobbies": lobbies, "players": players, "games": games}

@app.get("/games")
async def get_games():
    return {"games": games}


@app.get("/players")
async def get_players():
    return {"players": players}


@app.get("/lobbies")
async def get_lobbies():
    return {"lobbies": lobbies}

@app.post("/lobbies")
async def add_lobby(lobby: str):
    lobbies.append(lobby)
    return {"lobbies": lobbies}