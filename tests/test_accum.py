# This module contains basic unit tests for accum module.
import pytest
import sys
import os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)
from stuff.accum import Accumulator


@pytest.fixture
def accum():
    yield Accumulator()
    print("DONE...! wow")
# TEST


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_twice(accum):
    accum.add()
    accum.add()
    assert accum.count ==2


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10