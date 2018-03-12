import os

import falcon
from neomodel import config

from movie_graph import views



class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.register_routes()

        config.DATABASE_URL = os.environ.get(
            'DATABASE_URL',
            'bolt://neo4j:neo4j@database:7687')

    def register_routes(self):
        self.add_route('/', views.Index())

application = App()
