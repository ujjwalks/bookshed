from neomodel import config

from movie_graph.app import application


def test_app_sets_neo4j_url():
    assert config.DATABASE_URL == 'bolt://neo4j:neo4j@database:7687'
