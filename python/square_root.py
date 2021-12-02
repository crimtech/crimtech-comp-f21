import math

def square_root(n):
    # Write your code here!
    if type(n) != int or n < 0:
        return -1
    i = math.sqrt(n)
    return i

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()