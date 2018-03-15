from movie_graph.models import Person, Movie


def test_movies_has_relation_to_person():
    p = Person(name="Evan").save()
    m = Movie(title="Star Wars", released=1977).save()
    m.directors.connect(p)
    assert m.directors.single() == p
