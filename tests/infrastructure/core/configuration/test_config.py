from mediark.infrastructure.core.configuration import (
    load_config, build_config, DevelopmentConfig, ProductionConfig)


def test_load_config(config_file):
    result = load_config(config_file)
    assert result is not None
    assert isinstance(result, dict)


def test_load_config_missing_file(config_file):
    path = 'missing_config.json'
    result = load_config(path)
    assert result is None


def test_build_config_development(config_file):
    result = build_config(config_file, 'DEV')

    assert isinstance(result, DevelopmentConfig)


def test_build_config_production(config_file):
    result = build_config(config_file, 'PROD')

    assert isinstance(result, ProductionConfig)


def test_build_config_production_no_file():
    path = 'missing_config.json'
    result = build_config(path, 'PROD')

    assert isinstance(result, ProductionConfig)
