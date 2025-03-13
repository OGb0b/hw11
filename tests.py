import pytest
from main import OldServiceImpl, ServiceAdapter


def test_service_adapter():
    old_service = OldServiceImpl()
    adapter = ServiceAdapter(old_service)
    assert adapter.get_data() == "Adapted: Old Data Format"

