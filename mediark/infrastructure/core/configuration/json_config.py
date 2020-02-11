import multiprocessing
from collections import defaultdict
from typing import Dict, Any
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError
from pathlib import Path
from .development_config import DevelopmentConfig


class JsonConfig(DevelopmentConfig):
    def __init__(self):
        super().__init__()
        self['mode'] = 'JSON'
        self['gunicorn'].update({
            'workers': self.number_of_workers()
        })
        self['authentication'] = {
            "type": "jwt",
            "secret_file": Path.home().joinpath('sign.txt')
        }
        self['factory'] = 'JsonFactory'
        self['strategy'].update({
            "ImageRepository": {
                "method": "json_image_repository",
            },
            "AudioRepository": {
                "method": "json_audio_repository",
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