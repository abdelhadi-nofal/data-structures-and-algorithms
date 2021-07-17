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
    hashtable.add('hadi', 45)
    actual = hashtable.get('hadi')
    expected = 45
    assert actual == expected


def test_single_hash_fail():
    hashtable = HashTable()
    hashtable.add('hadi', 40)
    actual = hashtable.get('hadi')
    expected = 45
    assert actual != expected


def test_contains_pass_true():
    hashtable = HashTable()
    hashtable.add('hadi', 40)
    expected = hashtable.contains('hadi')
    actual = True
    assert actual == expected


def test_contains_pass_false():
    hashtable = HashTable()
    hashtable.add('hadi', 40)
    expected = hashtable.contains('Daniel')
    actual = False
    assert actual == expected


def test_contains_pass_with_collsion():
    hashtable = HashTable()
    hashtable.add('hadi', 40)
    hashtable.add('ahmad', 33)
    hashtable.add('moe', 11)
    expected = hashtable.contains('ahmad')
    actual = True
    assert actual == expected


def test_contains_fail():
    hashtable = HashTable()
    hashtable.add('hadi', 40)
    expected = hashtable.contains('Daniel')
    actual = True
    assert actual != expected


def test_add_multiple_hash_pass():
    hashtable = HashTable()
    hashtable.add('hadi', 45)
    hashtable.add('ahmad', 33)
    hashtable.add('moe', 11)
    actual = hashtable.get('moe')
    expected = 11
    assert actual == expected