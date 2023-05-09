import pytest


class TestArbitrary:
    @pytest.mark.pack
    @pytest.mark.unit
    def test_arbitrary1(self):
        assert True

    @pytest.mark.pack
    @pytest.mark.unit
    def test_arbitrary2(self):
        assert True

    @pytest.mark.pack
    @pytest.mark.rest
    def test_arbitrary3(self):
        assert True

    @pytest.mark.pack
    @pytest.mark.rest
    def test_arbitrary4(self):
        assert True
