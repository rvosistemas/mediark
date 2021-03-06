from typing import Dict, Any
from tenark.resolver import (
    resolve_cataloguer, resolve_provider, resolve_arranger)
from .tenant_supplier import TenantSupplier


class JsonTenantSupplier(TenantSupplier):

    def __init__(self, catalog_path: str,  directory_data: str,
                 directory_template='__template__') -> None:
        cataloguer = resolve_cataloguer({
            "cataloguer_kind": "json",
            "catalog_path": catalog_path
        })
        self.provider = resolve_provider({
            'cataloguer': cataloguer
        })
        self.arranger = resolve_arranger({
            'cataloguer': cataloguer,
            'provisioner_kind': 'directory',
            'provision_template': (
                str(directory_data) + f"/{directory_template}"),
            'provision_directory_zones': {
                "default": directory_data},
        })

    def get_tenant(self, tenant_id: str) -> Dict[str, Any]:
        return self.provider.get_tenant(tenant_id)

    def create_tenant(self, tenant_dict: Dict[str, Any]) -> None:
        self.arranger.create_tenant(tenant_dict)

    def search_tenants(self, domain):
        return self.provider.search_tenants(domain)

    def resolve_tenant(self, name: str) -> Dict[str, Any]:
        return self.provider.resolve_tenant(name)
