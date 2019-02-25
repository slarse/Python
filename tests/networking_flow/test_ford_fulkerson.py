import pytest

from networking_flow import ford_fulkerson


@pytest.fixture
def args():
    return (
        [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0],
        ],
        0,
        5,
    )


def test_ford_fulkerson(args):
    assert ford_fulkerson.FordFulkerson(*args) == 23
