#廖雪峰 使用list和tuple#
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# 请问以下变量哪些是tuple类型：
#c
a = ()
b = (1)
c = [2]
d = (3,)
e = (4,5,6)

#条件判断
#小明身高1.75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
# 并根据BMI指数：
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight/height/height
if bmi < 18.5 :
    print(bmi,'过轻')
elif 18.5 < bmi < 25:
    print(bmi,'正常')
elif 25 < bmi < 28:
    print(bmi,'过重')
elif 28 < bmi < 32:
    print(bmi,'肥胖')
else:
    print(bmi,'严重肥胖')


#循环
# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
l = ['Bart', 'Lisa', 'Adam']
for name in l :
    print('Hello,'+ name)