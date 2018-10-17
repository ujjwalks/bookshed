from movie_graph.models import Person, Movie, User, Book


def test_movies_has_relation_to_person():
    p = Person(name="Evan").save()
    m = Movie(title="Star Wars", released=1977).save()
    m.directors.connect(p)
    assert m.directors.single() == p

def test_user_has_relation_to_books():
    u = User(name="John Doe", email="johndoe@xyz.com").save()
    a = User(name="Yuval Harari", email="yuvalharari@xyz.com").save()
    b = Book(name="Sapiens").save()
    b.author.connect(a)
    u.book_own.connect(b)
    a.book_written.connect(b)
    assert b.author.single() == a
    assert u.book_own.single() == b
    assert a.book_written.single() == b