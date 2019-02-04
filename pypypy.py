numbers1= [1,3,5,7]
numbers2 = [2,4,6,8]

i=0
result = []
for i in range(len(numbers1)):
    result.append(numbers1[i]+numbers2[i])
print(result)

#파이썬 스러운 코드
print([(i+j)for (i,j) in zip(numbers1,numbers2)])


#튜플
tuple1 = (1+3)
tuple2 = (1+3,)
tuple4 = (3,)
print("튜플:",tuple1)

#packing
numbers = (1,2,3,4,5,6,7,8,9,10)
v1,v2,v3,v4 = numbers[-4:]
v1,v2,v3,v4, *others = numbers
print("팩킹이야:",numbers)

#dict
dict_values = {'blue': 10}
print("딕트:",dict_values)

del dict_values["blue"]
print("dict :",dict_values)