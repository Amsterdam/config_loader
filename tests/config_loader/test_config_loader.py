import os.path

import pytest

import config_loader


CONFIG_PATH = os.path.join('src', 'config_loader', 'config_example.yaml')
SCHEMA_PATH = os.path.join('src', 'config_loader', 'schema_example.yaml')


def test_default_value(monkeypatch):
    # language=rst
    """
    Load and validate a configuration.

    """
    monkeypatch.delenv('LOGLEVEL', raising=False)
    monkeypatch.setenv('DB_PASS', 'secret123')
    config = config_loader.load(
        CONFIG_PATH,
        SCHEMA_PATH
    )
    assert config['logging']['loggers']['authz_admin']['level'] == 'DEBUG'
    assert config['postgres']['password'] == 'secret123'


def test_missing_required_value(monkeypatch):
    # language=rst
    """
    Load and validate a configuration.

    """
    monkeypatch.delenv('LOGLEVEL', raising=False)
    monkeypatch.delenv('DB_PASS', raising=False)
    with pytest.raises(config_loader.ConfigError):
        config = config_loader.load(
            CONFIG_PATH,
            SCHEMA_PATH
        )


def test_change_default_value(monkeypatch):
    # language=rst
    """
    Load and validate a configuration.

    """
    monkeypatch.setenv('LOGLEVEL', 'WARNING')
    monkeypatch.setenv('DB_PASS', 'secret123')
    config = config_loader.load(
        CONFIG_PATH,
        SCHEMA_PATH
    )
    assert config['logging']['loggers']['authz_admin']['level'] == 'WARNING'
