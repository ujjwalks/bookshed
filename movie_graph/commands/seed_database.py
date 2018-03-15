#!/usr/bin/env python
import os

from neomodel import config, db


def seed():
    config.DATABASE_URL = os.environ.get('DATABASE_URL')
    with open('seed.cypher') as f:
        seed_query = f.read()
    db.cypher_query(seed_query)


if __name__ == '__main__':
    seed()
