

#class2
#인스턴스를 호출가능하도록 만들기
class Calculator2(object):
    def __init__(self,base):
        self.base = base
    def mysum(self,x,y):
        return self.base+x+y

calculator2 = Calculator2(10)
#print(calculator2(1,2)) #이건 안됨 ㅠㅠㅠㅠㅠ
print(calculator2.mysum(1,2))  

class Calculator(object):
    def __init__(self,base):
        self.base = base
    def __call__(self,x,y):
        return self.base + x + y

calculator = Calculator(10)
print(calculator(1,2))
print(calculator.__call__(1,2))    #이게 신기한거임 왜냐
#쓰는쪽은 함수처럼 쓰고 싶다는 가정하에 만든게 call임

#상태값을 유지하는 함수

class Calculator3(object):
    def __init__(self,base):
        self.base = base
    def __call__(self,x,y):
        self.base+=(x+y)
        return self.base

#상태값이 계속 변화함 허허허허
calc = Calculator3(10)
print(calc(1,2))
print(calc(1,2))
print(calc(1,2))
print(calc(1,2))