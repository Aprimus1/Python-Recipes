'''From a generator to another generator, passing trough a channel(grouper)'''



def caller(data):
    result = []
    group = grouper(result)
    next(group)
    for item in data:
        group.send(item)
    group.send(None)
    print('{:0.2f}'.format(result[0]))


def grouper(result):
    while True:
        foo = yield from averager()
        result.append(foo)

def averager():
    total = 0
    count = 0
    average = 0
    while True:
        received = yield
        if received is None:
            break
        total += received
        count += 1
        average = total/count
    return average

data = [10, 20, 40]

print(caller(data)) # --> 23.33
