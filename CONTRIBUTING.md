# Contributing

Developing new semantic assets such as ontologies and core vocabularies
happens writing turtle files (media-type: text/turtle) with extension `.ttl`.

Once you write or edit a `.ttl` files, you have to run a build process
that generates other serialization such as rdf+xml and jsonld.

To ensure quality assets, the repository comes with a series of tools
to ease QA checks such as `pre-commit` and converters:
all checks and buildings can be executed via docker.

For ontologies, tests are only run in the `latest/` directory of every asset, which is then compared with the directory referencing the latest
version of the asset.

To build your local copy, just run

        docker-compose up build

To run the tests, just run

        docker-compose up test-all

The repository is hosted on github and uses github actions to
test the developed stuff.
