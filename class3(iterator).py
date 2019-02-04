

#순회가능한 class 만들기
#순회가능한 객체
for ch in "hello world":
    print(ch)
print("==========================")
for i in [1,2,3]:
    print(i,i**2)

print("==========================")
#사전의 경우
mydict = {'a':1,'b':2}
for key in mydict:
    print(key)

print(mydict.keys())
print(mydict.values())

print("==========================")

for item in mydict.items():
    print(item)

print("=========================")

for key,values in mydict.items():
    print(key,values)

print("=========================")

#진짜 순회가능한 class 만들어보기

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self # iterator를 요구받고, 현 instance에서 next처리
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration # 남은 요소가 없을 때, StopIteration 강제 발생
        value = self.start
        self.start += 1
        return value # 다음 요소를 return


myrange = MyRange(0,3) 
iterator  = iter(myrange)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("===============================")

myrange2 = MyRange(0,3)
for i in myrange2:
    print(i)

