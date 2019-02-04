
def mygugu():
    for i in range(2,9,2):
        for j in range(1,10):
            print(i*j)


mygugu()

['{0} x {1} = {2}'.format(i, j, i*j) for j in range(1, 10) for i in range(2, 10, 2)]
