from neomodel import (
    ArrayProperty,
    IntegerProperty,
    StringProperty,
    StructuredNode,
    StructuredRel,
    RelationshipFrom
)


class Person(StructuredNode):
    name = StringProperty(required=True)


class ActorRel(StructuredRel):
    roles = ArrayProperty(StringProperty())


class ReviewerRel(StructuredRel):
    summary = StringProperty(required=True)


class Movie(StructuredNode):
    title = StringProperty(unique_index=True, required=True)
    tagline = StringProperty(required=False)
    released = IntegerProperty(required=True)

    directors = RelationshipFrom(Person, 'DIRECTED')
    actors = RelationshipFrom(Person, 'ACTED_IN', model=ActorRel)
    producers = RelationshipFrom(Person, 'PRODUCED')
    reviewers = RelationshipFrom(Person, 'REVIEWED', model=ReviewerRel)
    followers = RelationshipFrom(Person, 'FOLLOWS')
    writers = RelationshipFrom(Person, 'WROTE')
