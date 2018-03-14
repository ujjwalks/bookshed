from neomodel import (
    IntegerProperty, StringProperty,
    StructuredNode, RelationshipFrom
)


class Movie(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    tagline = StringProperty(required=False)
    released = IntegerProperty(required=True)

    directors = RelationshipFrom('movie_graph.models.Person', 'DIRECTED')
    actors = RelationshipFrom('movie_graph.models.Person', 'ACTED_IN')
    producers = RelationshipFrom('movie_graph.models.Person', 'PRODUCED')
    reviewers = RelationshipFrom('movie_graph.models.Person', 'REVIEWED')


class Person(StructuredNode):
    name = StringProperty(required=True)
