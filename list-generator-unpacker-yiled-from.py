a = [[[1, 2, 3, 4],1,2,3]]

def test_gen(array):
    for item in array:
        if isinstance(item,int):
            yield item
        else:
            yield from test_gen(item)

print(list(test_gen(a))) #-------> [1, 2, 3, 4, 1, 2, 3]
