from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from .config import Config
from pathlib import Path


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self['mode'] = 'DEV'
        self['gunicorn'].update({
            'limit_request_line': 0,
            'debug': True,
            'acesslog': '-',
            'loglevel': 'debug'
        })
        self["zones"] = {
            "default": {
                "dsn": 'dummy_connection://database'
            }
        }
        self['secrets'] = {
            "jwt": Path.home() / 'sign.txt'
        }
        self['authorization'] = {
            "dominion": "mediark"
        }
        self['factory'] = 'HttpFactory'

        self['strategy'] = {
            # Security
            "Authenticate": {
                "method": "middleware_authenticate"
            },
            "AuthProvider": {
                "method": "standard_auth_provider"
            },
            "SessionCoordinator": {
                "method": "session_coordinator"
            },

            # Query parser
            "QueryParser": {
                "method": "query_parser"
            },
            "IdService": {
                "method": "standard_id_service"
            },
            "AuthProvider": {
                "method": "standard_auth_provider"
            },
            # Tenancy
            "TenantProvider": {
                "method": "standard_tenant_provider"
            },
            "TenantSupplier": {
                "method": "memory_tenant_supplier"
            },

            "ImageFileStoreService": {
                "method": "memory_image_file_store_service"
            },
            "ImageRepository": {
                "method": "memory_image_repository",
            },
            "ImageFileStoreService": {
                "method": "directory_image_file_store_service"
            },
            "AudioFileStoreService": {
                "method": "directory_audio_file_store_service"
            },
            "ImageStorageCoordinator": {
                "method": "image_storage_coordinator",
            },
            "AudioFileStoreService": {
                "method": "memory_audio_file_store_service"
            },
            "AudioRepository": {
                "method": "memory_audio_repository",
            },
            "AudioStorageCoordinator": {
                "method": "audio_storage_coordinator",
            },
            "MediarkReporter": {
                "method": "memory_mediark_reporter",
            },
            "DirectoryLoadSupplier": {
                "method": "directory_load_supplier"
            },
            "MediarkReporter": {
                "method": "http_mediark_reporter",
            },
        }
