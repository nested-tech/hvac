#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gcp methods module."""
from hvac import exceptions
from hvac.api import VaultApiBase
from hvac.constants.aws import ALLOWED_CREDS_ENDPOINTS
from hvac.constants.gcp import DEFAULT_MOUNT_POINT


class Gcp(VaultApiBase):

    def generate_credentials(self, roleset, endpoint='key', mount_point=DEFAULT_MOUNT_POINT):
        if endpoint not in ALLOWED_CREDS_ENDPOINTS:
            error_msg = 'invalid endpoint argument provided "{arg}", supported types: "{allowed_endpoints}"'
            raise exceptions.ParamValidationError(error_msg.format(
                arg=endpoint,
                allowed_endpoints=', '.join(self.ALLOWED_CREDS_ENDPOINTS),
            ))

        api_path = '/v1/{mount_point}/{endpoint}/{roleset}'.format(
            mount_point=mount_point,
            endpoint=endpoint,
            roleset=roleset,
        )
        response = self._adapter.get(
            url=api_path
        )
        return response.json()
