from typing import Tuple
import pandas as pd
from datetime import datetime

from .db.models.player import Player
from .db.models.tournament import Tournament


def format_player(row: object, fname: str = 'X', lname: str = 'X.1', nationality: str = 'UNK', dob: str = '19000000', hand: str = 'U') -> Player:
    """Given row from jeff sackmans player csv formats to player object

    Args:
        row (object): DataFrame row 
        fname (str, optional): column containing first name. Defaults to 'X'.
        lname (str, optional): column containing last name. Defaults to 'X.1'.
        nationality (str, optional): column containing nationality. Defaults to 'UNK'.
        dob (str, optional): column containing date of birth. Defaults to '19000000'.
        hand (str, optional): column containing hand. Defaults to 'U'.

    Returns:
        Player: player instance
    """
    return Player(first_name=row[fname],
                  last_name=row[lname],
                  nationality=row[nationality],
                  dob=datetime.strptime(str(row[dob]), '%Y%m%d'),
                  hand=row[hand])


def format_tournament(row: object, name: str = 'tourney_name', surface: str = 'surface', draw_size: str = 'draw_size', level: str = 'tourney_level', start_date: str = 'tourney_date') -> Tournament:
    """Given row from jeff sackmans matches csv formats to tournament object

    Args:
        row (object): DataFrame row
        name (str, optional): column containing tournament name. Defaults to 'tourney_name'.
        surface (str, optional): column containing surface type. Defaults to 'surface'.
        draw_size (str, optional): column containing draw size. Defaults to 'draw_size'.
        level (str, optional): column containing tournament level. Defaults to 'tourney_level'.
        start_date (str, optional): column containing tournament start date. Defaults to 'tourney_date'.

    Returns:
        Tournament: tournament instance
    """
    return Tournament(name=row[name],
                      surface=row[surface],
                      draw_size=row[draw_size],
                      level=row[level],
                      start_date=datetime.strptime(str(row[start_date]), '%Y%m%d'))