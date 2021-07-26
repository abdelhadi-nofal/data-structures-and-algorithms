from repeated_word import __version__
from repeated_word.repeated_word import word_repeated


def test_version():
    assert __version__ == '0.1.0'


def test_repated_word():
    the_string = 'my name is hadi nofal , hadi is software engineer , is'

    result = word_repeated(the_string)
    assert result == 'is'