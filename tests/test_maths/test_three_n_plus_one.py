import pytest

from maths import three_n_plus_one


def test_n31_with_43():
    expected = (
        [
            43,
            130,
            65,
            196,
            98,
            49,
            148,
            74,
            37,
            112,
            56,
            28,
            14,
            7,
            22,
            11,
            34,
            17,
            52,
            26,
            13,
            40,
            20,
            10,
            5,
            16,
            8,
            4,
            2,
            1,
        ],
        29,
    )
    assert three_n_plus_one.n31(43) == expected


def test_n31_last_element():
    assert three_n_plus_one.n31(98)[0][-1] == 1
