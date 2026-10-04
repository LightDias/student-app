import pytest
from app import add_student, count_students


def test_add_student():
    assert add_student([], "Aidar") == ["Aidar"]


def test_count_students():
    assert count_students(["A", "B"]) == 2


def test_empty_name():
    with pytest.raises(ValueError):
        add_student([], "  ")