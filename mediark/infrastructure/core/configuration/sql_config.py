import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path
from .development_config import DevelopmentConfig


class SqlConfig(DevelopmentConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = 'PROD'
        self['gunicorn'].update({
            'workers': self.number_of_workers()
        })
        self['authentication'] = {
            "type": "jwt",
            "secret_file": Path.home().joinpath('sign.txt')
        }
        self['tenancy'] = {
            "dsn": (
                "postgresql://mediark:mediark"
                "@localhost/mediark")
        }
        self["zones"] = {
            "default": {
                "dsn": ("postgresql://mediark:mediark"
                        "@localhost/mediark"),
                "pool": {}
            }
        }
        self['factory'] = 'SqlFactory'
        self['strategy'].update({
            # Parser
            "SqlParser": {
                "method": "sql_query_parser"
            },

            # Connections
            "ConnectionManager": {
                "method": "sql_connection_manager",
            },

            "TransactionManager": {
                "method": "sql_transaction_manager",
            },


            # Repositories
            "ImageRepository": {
                "method": "sql_image_repository",
            },
            "AudioRepository": {
                "method": "sql_audio_repository",
            },

            # Tenancy

            "TenantProvider": {
                "method": "standard_tenant_provider"
            },

            "TenantSupplier": {
                "method": "schema_tenant_supplier"
            },
        })

    def number_of_workers(self):
        return (multiprocessing.cpu_count() * 2) + 1