import pandas as pd
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

PLAYER_URL = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_2026.csv"
)

GAMES_URL = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "schedules/games.csv"
)

def extract_data(url:str)-> pd.DataFrame:
    """
    Extracts data from a given URL and returns it as a pandas DataFrame.

    Args:
        url (str): The URL to extract data from.

    Returns:
        pd.DataFrame: The extracted data as a pandas DataFrame.
    """
    return pd.read_csv(url)

def main():
    # Extract data from the URLs
    players = extract_data(PLAYER_URL)
    games = extract_data(GAMES_URL)

    games['gameday']= pd.to_datetime(games['gameday'], format='%Y-%m-%d')
    # Save the extracted data to CSV files in the data directory
    players.to_csv(DATA_DIR / "players.csv", index=False)
    games.to_csv(DATA_DIR / "games.csv", index=False)

