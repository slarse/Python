import pytest

from other.tower_of_hanoi import moveTower


@pytest.fixture
def expected_output_lines():
    return [
        "moving disk from A to B",
        "moving disk from A to C",
        "moving disk from B to C",
        "moving disk from A to B",
        "moving disk from C to A",
        "moving disk from C to B",
        "moving disk from A to B",
    ]


def test_move_tower(capsys, expected_output_lines):
    moveTower(3, "A", "B", "C")

    captured = capsys.readouterr()
    lines = [line for line in captured.out.splitlines()]
    assert lines == expected_output_lines
