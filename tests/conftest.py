import pytest


@pytest.fixture
def time_mock(mocker):
    return mocker.patch("time.perf_counter")
