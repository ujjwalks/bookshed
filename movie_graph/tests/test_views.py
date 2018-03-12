import falcon
from falcon import testing

from movie_graph.app import application

import pytest


@pytest.fixture
def client():
    return testing.TestClient(application)


def test_index(client):
    response = client.simulate_get('/')

    assert response.json == {u'message': u'Hello world!'}
    assert response.status == falcon.HTTP_OK

