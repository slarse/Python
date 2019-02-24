from other.detecting_english_programmatically import isEnglish


class TestDetectingEnglishProgrammatically:
    def test_is_english(self):
        assert isEnglish("Hello World")

    def test_is_not_english(self):
        assert not isEnglish("llold HorWd")
