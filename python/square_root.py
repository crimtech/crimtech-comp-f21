import math

def square_root(n):
    # Write your code here!
    # Case of negative or not int
    try:
        n = int(n)
    except:
        return -1
    if (n < 0):
        return -1
    
    # int > 0
    else:
        return n**0.5
    

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()