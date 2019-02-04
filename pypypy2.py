##들여쓰기

for i  in range(4):
    print(i)

for i in range(4):
    print(i)


#주석
names = {
    'Tom':10,
    'Steve':12,
#   'hanmin': 26,
}

print(names)

def mysum(a,b,c):
    ''' 세인자를 받아서, 더한 값을 리턴을 해줍니다.
    '''
    return a+b+c


print(mysum.__doc__)
print(mysum(1,2,3))