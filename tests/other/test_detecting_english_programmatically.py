from other.detecting_english_programmatically import isEnglish


def test_is_english():
    assert isEnglish("Hello World")


def test_is_not_english():
    assert not isEnglish("llold HorWd")
