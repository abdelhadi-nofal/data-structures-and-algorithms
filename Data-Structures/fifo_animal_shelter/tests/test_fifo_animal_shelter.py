from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Node,AnimalShelter
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_cats_and_dogs():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.dequeue()
    assert shelter.front.value == 'cat'


def test_enqueue_other_animals():
    shelter = AnimalShelter()
    shelter.enqueue('bird')
    assert shelter.front.value == ValueError
