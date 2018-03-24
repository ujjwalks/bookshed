Movie Graph README
==================

.. image:: https://secure.travis-ci.org/efagerberg/movie_graph.png
    :target: https://secure.travis-ci.org/efagerberg/movie_graph/


.. image:: https://readthedocs.org/projects/movie_graph/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://movie_graph.readthedocs.io/en/latest/?badge=latest


An experiment in making an API with Falcon around a Neo4J backend.

Based off the Neo4J Movie Graph example.

Setup
------

.. code-block:: bash

    $ make

Seed Database
-------------

In order to get the sample graph database loaded up run:

.. code-block:: bash

    $ make seed

Tests
-----

.. code-block:: bash

    $ make tests
