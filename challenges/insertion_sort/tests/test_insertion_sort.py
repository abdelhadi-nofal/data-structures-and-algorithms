from insertion_sort import __version__
from insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'




def test_insertion_sort():
    actual = insertion_sort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected
