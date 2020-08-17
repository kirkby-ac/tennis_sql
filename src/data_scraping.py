import pandas as pd

PLAYER_URL = "https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_players.csv"
WTA_URL = "https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_matches_{}.csv"
ITF_URL = "https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_matches_qual_itf_{}.csv"


def get_raw_players(n_players: int = None) -> pd.DataFrame:
    '''
    Gets all WTA players in Jeff Sackmans WTA data

    args:
        n_players: (ignore just used for testing) Number of players to return

    returns:
        dataframe of players
    '''
    return pd.read_csv(
        PLAYER_URL,
        mangle_dupe_cols=True,  # duplicate columns i.e. X, X -> X, X.1
        nrows=n_players,
    )


def get_raw_games(year_from: int, year_to: int, n_games: int = None) -> pd.DataFrame:
    '''
    Gets all WTA and ITF games

    args:
        n_games: (ignore just used for testing) returns most recent WTA matches

    returns:
        raw dataframe of games
    '''
    if n_games:
        return pd.read_csv(WTA_URL.format(year_to), encoding="ISO-8859-1", nrows=n_games)
    else:
        data = None
        for year in range(year_from, year_to + 1):
            new_wta = pd.read_csv(WTA_URL.format(year), encoding="ISO-8859-1")
            new_itf = pd.read_csv(ITF_URL.format(year), encoding="ISO-8859-1")

            new_wta['source'] = 'W'
            new_itf['source'] = 'I'

            if isinstance(data, pd.DataFrame):
                data = data.append(new_wta, ignore_index=True)
            else:
                data = new_wta

            data = data.append(new_itf, ignore_index=True)
        return data
