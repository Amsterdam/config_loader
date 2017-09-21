.. reference this page as :ref:`index` (from which it's included)


Datapunt Config Loader
======================

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/badge/license-MPLv2.0-blue.svg
   :target: https://www.mozilla.org/en-US/MPL/2.0/


Usage
=====

Module that loads configuration settings from a yaml file.

.. code-block:: python

    import config_loader
    import logging

    CONFIG = config_loader.load(
        path_to_config_file,
        path_to_config_schema_file
    )
    logging.config.dictConfig(CONFIG['logging'])

This package comes with an example JSON schema file :file:`schema_example.json`
that contains a schema definition for a dict that can be passed into
`logging.config.dictConfig`.


Contributing
============

To get your development environment up and running:

.. code-block:: bash

    # Clone the repository:
    git clone git@github.com:Amsterdam/config_loader.git
    cd config_loader

    # Create and activate a virtual environment, for example:
    python3.6 -m venv --copies --prompt authz_admin .venv
    source ./.venv/bin/activate

    make          # defaults to `make dist`
    make dist
    make release  # Don't forget to version bump in setup.py first.
    make build
    make test
    make testcov
    make clean


Conventions
-----------

*   We use PyTest for tests.
*   PyTest can be integrated with SetupTools (see
    https://docs.pytest.org/en/latest/goodpractices.html). We don’t do this.
*   Common commands for builds, distributing, packaging, documentation etcetera
    are in :file:`Makefile` and :file:`sphinx/Makefile`.
*   RST files and docstrings are indented with 4 spaces.
*   Globals must be immutable.
*   We follow Google’s formatting standard in docstrings.
*   Docstrings are formatted like this:

    .. code-block:: python

        """This is a one-line docstring."""
        """One line description, terminated with a period.

        More info, with a trailing empty line.

        """
