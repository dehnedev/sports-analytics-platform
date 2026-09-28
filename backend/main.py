from fastapi import FastAPI
from nfl_model import predict_nfl_game

app = FastAPI()


@app.get("/nfl/predict")
def get_nfl_prediction(team1: str, team2: str):
    return predict_nfl_game(team1, team2)
