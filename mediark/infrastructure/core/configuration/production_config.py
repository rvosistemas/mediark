import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path
from .development_config import DevelopmentConfig


class ProductionConfig(DevelopmentConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = 'PROD'
        self['gunicorn'].update({
            'workers': self.number_of_workers()
        })
        self['authentication'] = {
            "type": "jwt",
            "secret_file": str(Path.home().joinpath('sign.txt'))
        }
        self['tenancy'] = {
            'json':  Path.home() / 'tenants.json'
        }
        self['data'] = {
            "json": {
                "default": str(Path.home().joinpath('data'))
            }
        }
        self['factory'] = 'HttpFactory'
        self['strategy'].update({
            "JwtSupplier": {
                "method": "jwt_supplier"
            },
            "ImageRepository": {
                "method": "shelve_image_repository",
            },
            "ImageFileStoreService": {
                "method": "directory_image_file_store_service"
            },
            "AudioRepository": {
                "method": "shelve_audio_repository",
            },
            "AudioFileStoreService": {
                "method": "directory_audio_file_store_service"
            },
            "MediarkReporter": {
                "method": "http_mediark_reporter",
            },

            # Tenancy

            "TenantProvider": {
                "method": "standard_tenant_provider"
            },

            "TenantSupplier": {
                "method": "json_tenant_supplier"
            },
        })

    def number_of_workers(self):
        return (multiprocessing.cpu_count() * 2) + 1
