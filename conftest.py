import pytest


@pytest.fixture(autouse=True)
def project_fixture():
    print("\nBefore all tests")
    yield
    print("\nAfter all tests")