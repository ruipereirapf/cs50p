from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("What's Your Name?") == "Wht's Yr Nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("RUI PEDRO FERNANDES PEREIRA") == "R PDR FRNNDS PRR"