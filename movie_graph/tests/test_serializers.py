import json

from unittest.mock import patch

from neomodel import StructuredNode
import pytest

from movie_graph.models import Movie, Person
from movie_graph.serializers import StructuredThingSerializer


@pytest.fixture()
def movie():
    yield Movie(title="Space Cop", released=2016).save()


@pytest.fixture()
def mock_defined_properties():
    path = 'neomodel.StructuredNode.defined_properties'
    with patch(path, autospec=True) as m:
        yield m


def test_serializes_node(movie):
    """StructuredThingSerializer should serialize all fields,
    and relationships of a StructuredNode by default"""
    p = Person(name="Mike Stoklasa").save()
    movie.directors.connect(p)
    actor_rel = movie.actors.connect(p, {'roles': ['Detective Ted Cooper']})

    expected = json.dumps({
        'id': movie.id,
        'title': movie.title,
        'tagline': movie.tagline,
        'released': movie.released,
        'directors': [
            {'id': p.id,
             'name': p.name,
             'followers': p.followers.all()}
        ],
        'actors': [
            {'id': p.id,
             'name': p.name,
             'followers': p.followers.all(),
             'relationships': [{'roles': actor_rel.roles}]}
        ],
        'producers': movie.producers.all(),
        'reviewers': movie.reviewers.all(),
        'writers': movie.writers.all()
    })
    actual = StructuredThingSerializer(movie).serialized_data
    assert actual == expected


def test_serializes_certain_fields(movie):
    """"StructuredThingSerializer should exclude fields not
    declared in fields"""
    expected = json.dumps({
        'title': movie.title,
        'released': movie.released
    })
    actual = StructuredThingSerializer(
        movie, fields=('title', 'released')).serialized_data
    assert actual == expected


def test_serializes_structured_node_without_prop_or_rel_defs():
    """StructuredThingSerializer should handle a StructuredNode
    without any properties or relationship definitions."""
    class Foo(StructuredNode):
        pass
    x = Foo().save()
    expected = json.dumps({'id': x.id})
    actual = StructuredThingSerializer(x).serialized_data
    assert actual == expected


def test_raises_on_non_property_non_rel_def(mock_defined_properties):
    """StructuredThingSerializer should raise ValueError
    when a prop that is passed is not a Property or
    RelationshipDefinition"""
    class Foo(StructuredNode):
        pass
    x = Foo().save()
    props = {'foo': 'bar'}
    mock_defined_properties.return_value = props
    expected_msg = "Undexpected property received: {}".format(props)
    with pytest.raises(ValueError, message=expected_msg):
        StructuredThingSerializer(x)
