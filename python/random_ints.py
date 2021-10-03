import random

def random_ints():
    l = []
    while True:
        m = (int) (random.random()*10)
        if m == 0:
            m = m + 1
        l.append(m)
        if m == 7:
            return l

# l = []
#    while True:
#        m = random.randint(1, 10)
#        l.append(m)
#        if m == 7:
#            return l

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