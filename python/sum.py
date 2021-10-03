def sum(l, N):
    # Write your code here!
    # make set
    # traverse list checking if N - l[i] is in set
    # if not add number to set

    set_list = set()
    for number in l:
        if (N- number) in set_list:
            return True
        set_list.add(number)
    return False


def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()