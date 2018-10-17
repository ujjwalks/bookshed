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
    followers = RelationshipFrom('Person', 'FOLLOWS')


class ActorRel(StructuredRel):
    roles = ArrayProperty(StringProperty())


class ReviewerRel(StructuredRel):
    summary = StringProperty(required=True)


class Movie(StructuredNode):
    title = StringProperty(unique_index=True, required=True)
    tagline = StringProperty()
    released = IntegerProperty(required=True)

    directors = RelationshipFrom(Person, 'DIRECTED')
    actors = RelationshipFrom(Person, 'ACTED_IN', model=ActorRel)
    producers = RelationshipFrom(Person, 'PRODUCED')
    reviewers = RelationshipFrom(Person, 'REVIEWED', model=ReviewerRel)
    writers = RelationshipFrom(Person, 'WROTE')


class CommunityRel(StructuredRel):
    state = StringProperty(required=False)

    
class OwnBookRel(StructuredRel):
    lent_to = StringProperty(required=False)


class Book(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    summary = StringProperty(required=False)
    published = IntegerProperty(required=False)
    tags = ArrayProperty(required=False)
    author = RelationshipFrom('User', 'AUTHOR')


class User(StructuredNode):
    name = StringProperty(required=True)
    email = StringProperty(unique_index=True, required=True)
    community = RelationshipFrom('User', 'COMMUNITY', model=CommunityRel)
    book_own = RelationshipFrom(Book, 'OWNS', model=OwnBookRel)
    book_written = RelationshipFrom(Book, 'WROTE')

