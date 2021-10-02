import random

def random_ints():
    l = []
    found = False
    while not found:
        nr = random.randint(1, 10)
        if nr != 7:
            l.append(nr)
        else:
            l.append(7)
            found = True
    return l

def test():
    N = 10000
    total_length = 0
    for i in range(N):
        l = random_ints()
        assert not 0 in l
        assert not 11 in l
        assert l[-1] == 7
        total_length += len(l)
    assert abs(total_length / N - 10) < 1 # checks that the length of the random strings are reasonable.
    print("Success!")

if __name__ == "__main__":
    test()