# test_app.py
import pytest
from app import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(-1, -1) == 0

if __name__ == "__main__":
    pytest.main()
