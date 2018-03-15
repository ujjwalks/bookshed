from unittest.mock import patch
import pytest

from movie_graph.commands.seed_database import seed


BASE_MOCK_PATH = 'movie_graph.commands.seed_database'


@pytest.fixture()
def mock_open():
    with patch('{}.open'.format(BASE_MOCK_PATH)) as m:
        yield m


@pytest.fixture()
def mock_db():
    with patch('{}.db'.format(BASE_MOCK_PATH), autospec=True) as m:
        yield m


def test_seeds_database_with_expected_cypher_file(mock_open, mock_db):
    """seed_database should open 'seed.cypher' and run the queries inside it"""
    mock_open.return_value.__enter__.return_value.read.return_value = 'foo'
    seed()
    mock_open.assert_called_once_with('seed.cypher')
    mock_db.cypher_query.assert_called_once_with('foo')
