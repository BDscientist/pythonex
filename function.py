

number=10
result1 = number *2
result2 = result1 **3
result3 = result2 **10
print(result3)

number = 20
result1 = number *2
result2 = result1 **3
result3 = result2 **10
print(result3)
print("==========================")

def calculate(number):
    result1 = number *2
    result2 = result1 **3
    result3 = result2 **10
    return result3  

calculate(3)

##상수
SIZE  =10
def calc2(x,y):
    return(x+y)*SIZE


calc2(3,4)
print("=================")


#인자인자
def fn_with_positional_argments(name,age):
    print("당신의 이름은 {}이며,나이는 {}입니다.".format(name,age))


fn_with_positional_argments('Tom',10)


#인자를 무제한으로 받고싶을때
#packing
def fn2(*color):
    for color in color:
        print(color)
fn2()
fn2('white')
fn2('white','yellow')
print("======================")


#unpacking 먼저 정의를 해주고 함수안에 넣는방식
colors = ['white','yellow']
fn2(*colors)
fn2('brown','pink',*colors)
print("====================")
#가변인자

def fn2(**scores):
    for key,score in scores.items():
        print(key,score)

fn2(apple=10,orange=5)
fn2(apple=10,orange=5,banana=8)
fn2(apple=10,orange=5,banana=8,mango=9)

print("=====================")

def fn3(apple=0, **scores):
    print('apple:',apple)
    for key,score in scores.items():
        print(key,score)

fn3(apple=10,orange=5,banana=9)
fn3(apple=5,orange=9,banana=9,tomato=100)

print("======================")
#인자를 넘길때는 unpacking 으로 함 그리고 
#튜플이나 리스트는 * <-이걸로 넘겨주고 dict는 **<-이걸로 넘겨줌

'''
colors = ['white','yellow']
scores = {'apple':10 , 'orange':5}
fn2(*colors , **scores)
'''
#람다 함수 (익명함수)
lambda x,y: x+y
(lambda x,y:x+y)(1,2)

def mysum(x,y):
    return x+y
mysum2 = lambda x,y:x+y
mysum3 = lambda *args : sum(args)

print(mysum(1,2))
print("=======")
print(mysum2(1,2))
print("========")
print(mysum3(1,2,3,4,5,6,7,8,9))
print("====================")

#high order function(고차함수) 존나 신기하다 동적할당!!
def base_calc(base):
    wrap = lambda x,y:base+x+y
    return wrap
calc_10 = base_calc(10) #이러면 calc_10은 wrap을 갖게되고 10이라는 숫자를가짐
print(calc_10(1,2))
print(calc_10(1,10))


