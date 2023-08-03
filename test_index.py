import pytest
from src.index import root, health_check

def test_root():
    assert root() == {"message": "Ok"}

def test_health_check():
    assert health_check() == {"status": "Service is running"}
    