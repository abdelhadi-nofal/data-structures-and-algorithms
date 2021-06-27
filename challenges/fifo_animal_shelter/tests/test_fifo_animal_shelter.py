from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Node,AnimalShelter
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_cats_and_dogs():
    shelter = AnimalShelter()
    shelter.enqueue('spike','dog')
    shelter.enqueue('sahsa','cat')
    shelter.enqueue('spike2','dog')
    shelter.enqueue('cherry','cat')
    shelter.dequeue()
    assert shelter.front.name == 'sahsa'


# def test_enqueue_other_animals():
#     shelter = AnimalShelter()
#     shelter.enqueue('bird')
#     assert shelter.front.value == ValueError