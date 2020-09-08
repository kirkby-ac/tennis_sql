import pytest

from src.db.db import DBClient
from src.db.schema.base import Base
from src.data_scraping import get_raw_players, get_raw_games


TEST_DB = 'test_db'


@pytest.fixture(scope='session')
def db_client():
    # db instance
    db_client = DBClient(db_name=TEST_DB)
    yield db_client
    # teardown delete all `Base` created test_db tables
    db_client.session.close()
    with db_client.engine.connect() as conn:
        Base.metadata.drop_all(conn, checkfirst=False)


@pytest.fixture(scope='session')
def sample_players():
    return get_raw_players(n_players=5)


@pytest.fixture(scope='session')
def sample_games():
    return get_raw_games(2020, 2020, n_games=5)
