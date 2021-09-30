def sum(l, N):
    # Write your code here!

    my_range = range(len(l))
    for i in my_range:
        for j in my_range:
            if l[i] + l[j] == N and i != j:
                return True

    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
