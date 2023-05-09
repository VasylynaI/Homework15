import pytest


@pytest.fixture(scope='class', autouse=False)
def class_fixture():
    print('\n=== Starting class tests ===')
    yield
    print('\n=== Ending class tests ===')


@pytest.mark.usefixtures('class_fixture')
class TestFromClass:

    @pytest.mark.from_class
    def test_1(self):
        pass

    @pytest.mark.from_class
    def test_2(self):
        pass

    @pytest.mark.from_class
    def test_3(self):
        pass

    @pytest.mark.from_class
    def test_4(self):
        pass

    @pytest.mark.from_class
    def test_5(self):
        pass
