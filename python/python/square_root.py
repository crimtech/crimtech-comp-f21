import math

def square_root(n):
    #n = input("Enter number:")
    if type(n) == int and n >= 0:
        n = n**0.5
    else:
        n = -1
    #print(n)
    return n

def test():
    assert square_root(4) == 2
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()