

#객체지향법
#class 쓰는법 앞에 대문자로하세요
class cirlce:
    pass
class favorite_article:
    pass
class Circle:
    pass
class Favorite_article:
    pass

#circle 클래스 로직구현#
from math import sqrt

class Circle(object):
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius= radius

    def area(self):
        return self.radius **2

    def distance(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)-(self.radius+other.radius)



circle1  = Circle(0,20,3)
print("circle1의 넓이:",circle1.area())

circle2=Circle(100,-40,10)
print("circle2의 넓이:",circle2.area())

print("circle1의 길이:",circle1.distance(circle2))


#person 클래스 구현

class Person(object):
    def __init__(self,name,age,region):
        self.name=name
        self.age=age
        self.region = region
    def say_hello(self):
        print("안녕하세요!!!{}님 {}에서 오셧군요".format(self.name,self.region))

    def move_to(self,region):
        print("{}에서 {}으로 이사합니다".format(self.region,region))
        self.region = region

tom = Person('Tom',10,'Seoul')
steve = Person('Steve',10,'Pusan')

steve.move_to('Canada')
steve.say_hello()


#dog 클래스 인스턴스 변수 선언

class Dog:
    def __init__(self):
        self.trick = []
    def add_trick(self,trick):
        self.trick.append(trick)

dog1 = Dog()
dog1.add_trick('roll over')

dog2 = Dog()
dog2.add_trick('play dead')

print(dog1.trick)
print(dog2.trick)

#자바의 private이랑 같은기능 .__  <-이기능
class Person:
    def __init__(self,name):
        self.__name=name
    
    def say_hello2(self):
        print("안녕{}.".format(self.__name))

# 이거 안되는거임 print(tom.__name)
#tom =  Person('tom')
#바깥에서 접근할땐 앞에 언더바하나에 클래스명 쓰고 그다음언더바 2개한다음 함수호출임
tom._Person__name 

tom.say_hello2()