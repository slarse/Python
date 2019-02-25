import pytest

from networking_flow import minimum_cut


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


def test_minimum_cut(args):
    assert minimum_cut.mincut(*args) == [(1, 3), (4, 3), (4, 5)]
