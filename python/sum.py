def sum(l, N):
    # Write your code here!
    duplicates = l 
    l = set(l)
    for x in l:
        duplicates.remove(x)
    for x in l:
        for y in l:
            if(x==y):
                if(y in duplicates and x+y==N):
                    return True
            else:
                if(x+y==N):
                    return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
