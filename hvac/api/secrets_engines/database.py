#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Database methods module."""
from hvac.api.vault_api_base import VaultApiBase

from hvac.constants.database import DEFAULT_MOUNT_POINT, ALLOWED_CREDS_ENDPOINT


class Database(VaultApiBase):

    def generate_credentials(self, role, mount_point=DEFAULT_MOUNT_POINT):
        api_path = '/v1/{mount_point}/{endpoint}/{role}'.format(
            mount_point=mount_point,
            endpoint=ALLOWED_CREDS_ENDPOINT,
            role=role,
        )
        response = self._adapter.get(
            url=api_path
        )
        return response.json()
