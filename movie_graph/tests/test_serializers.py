import json

import pytest

from movie_graph.models import Movie, Person
from movie_graph.serializers import StructuredNodeSerializer


@pytest.fixture()
def movie():
    yield Movie(title="Space Cop", released=2016).save()


def test_serializes_node(movie):
    """StructuredNodeSerializer should serialize all fields,
    and relationships of a StructuredNode by default"""
    p = Person(name="Mike Stoklasa").save()
    movie.directors.connect(p)
    rel = movie.actors.connect(p, {'roles': ['Detective Ted Cooper']})

    expected = json.dumps({
        'id': movie.id,
        'title': movie.title,
        'tagline': movie.tagline,
        'released': movie.released,
        'directors': [
            {'id': p.id,
             'name': p.name,
             'followers': []}
        ],
        'actors': [
            {'id': p.id,
             'name': p.name,
             'followers': []}
        ],
        'producers': [],
        'reviewers': [],
        'writers': []

    })
    actual = StructuredNodeSerializer(movie).serialized_data
    assert actual == expected


def test_serializes_certain_fields(movie):
    """"StructuredNodeSerializer should exclude fields not
    declared in fields"""
    expected = json.dumps({
        'title': movie.title,
        'released': movie.released
    })
    actual = StructuredNodeSerializer(
        movie, fields=('title', 'released')).serialized_data
    assert actual == expected
