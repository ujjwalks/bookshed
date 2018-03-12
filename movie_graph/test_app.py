import falcon
from falcon import testing
import pytest

from movie_graph.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_index(client):
    response = client.simulate_get('/')

    assert response.json == {u'message': u'Hello world!'}
    assert response.status == falcon.HTTP_OK
