from queue_with_stacks import __version__
import pytest
from queue_with_stacks.queue_with_stacks import Node,Stack,PseudoQueue


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue():
    pseudoq = PseudoQueue()
    pseudoq.enqueue(1)
    pseudoq.enqueue(2)
    pseudoq.enqueue(3)
    assert pseudoq.stack2.peek() == 1


def test_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    pseudo.dequeue()
    pseudo.dequeue()
    pseudo.dequeue()
    assert pseudo.stack2.peek() == 4



