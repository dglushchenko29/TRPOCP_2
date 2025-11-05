__version__ = "1.0.0"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("All tests passed!")

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    print("Multiply tests passed!")

if __name__ == "__main__":
    test_add()
    test_multiply()
