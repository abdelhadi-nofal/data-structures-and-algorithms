from hashtable import __version__
from hashtable.hashtable import HashTable


def test_version():
    assert __version__ == '0.1.0'


def test_hashtable_default_size():
    hashtable = HashTable()
    actual = hashtable.size
    expected = 1024
    assert actual == expected


def test_hashtable_custom_size():
    hashtable = HashTable(30)
    actual = hashtable.size
    expected = 30
    assert actual == expected


def test_hashtable_custom_size_fail():
    hashtable = HashTable(30)
    actual = hashtable.size
    expected = 35
    assert actual != expected


def test_single_hash_pass():
    hashtable = HashTable()
    hashtable.add('Chuck', 45)
    actual = hashtable.get('Chuck')
    expected = 45
    assert actual == expected


def test_single_hash_fail():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    actual = hashtable.get('Chuck')
    expected = 45
    assert actual != expected


def test_contains_pass_true():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Chuck')
    actual = True
    assert actual == expected


def test_contains_pass_false():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Daniel')
    actual = False
    assert actual == expected


def test_contains_pass_with_collsion():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    hashtable.add('kcuhC', 33)
    hashtable.add('Ckcuh', 11)
    expected = hashtable.contains('kcuhC')
    actual = True
    assert actual == expected


def test_contains_fail():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Daniel')
    actual = True
    assert actual != expected


def test_add_multiple_hash_pass():
    hashtable = HashTable()
    hashtable.add('Chuck', 45)
    hashtable.add('kcuhC', 33)
    hashtable.add('Ckcuh', 11)
    actual = hashtable.get('Ckcuh')
    expected = 11
    assert actual == expected