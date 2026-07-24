"""
Provider Factory
"""

from app.core.config import settings
from app.providers.gcp_provider import GCPProvider
from app.providers.mock_provider import MockProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        if settings.provider.lower() == "gcp":
            return GCPProvider()

        return MockProvider()