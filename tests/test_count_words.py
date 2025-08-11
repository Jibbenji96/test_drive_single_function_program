import pytest
from lib.count_words import *

def test_returns_an_empty_string():
    assert count_words("") == ""



def test_returns_a_word_count():
    assert count_words("hello my name is ben")
    assert count_words("   whitespace and trailing spaces   ") == 4


