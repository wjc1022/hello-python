#输入一个数，判断是否是质数
# num = int(input('请输入一个数字'))
# if num < 1:
#     print('不是质数')
# if num == 1:
#     print('是质数') 
# if num == 2:
#     print('是质数') 
# j=True
# for m in range(2,num):
#     if num % m == 0:
#         j=False
#         break
# if j :
#     print('是质数')
# else:
#     print('no是质数')

# num = int(input('请输入一个数字'))
# if num < 1:
#     print('不是质数')
# if num == 1:
#     print('是质数') 
# if num == 2:
#     print('是质数') 
# for m in range(2,num):
#     if num % m == 0:
#         print('no是质数')
#         break
# else:
#     print('是质数')


# 1.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
# for a in range (1,5):
#     for b in range (1,5):
#         if b==a :
#             continue
#         for c in range (1,5):
#             if c==a or c==b:
#                 continue
#             print(a,b,c)

# 2.题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

i=int(input('请输入当月利润（万元）')
if i < 10:
    bonus=0.1*i 
    print('奖金总数为：',bouns)
if i>10 and i<20 :
    bonus=1+(i-10)*0.075


# !/usr/bin/python
# -*- coding: UTF-8 -*-
 
# i = int(raw_input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print (i-arr[idx])*rat[idx]
#         i=arr[idx]
# print r
