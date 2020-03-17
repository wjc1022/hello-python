# for i in range(1,101):
#     if i%15 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# # 思考题 请用4.4中学习的for else的方式做一下BizzFuzz
# for i in range(1,101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#         continue
#     elif i % 3 ==0:
#         print('Fizz')
#         continue
#     elif i % 5 ==0: 
#         print('Buzz')
#         continue
#     else:
#         print(i)

# 预习题 将FizzBuzz的代码包装成一个函数，输入一个数字，报数到指定数字的函数
def FizzBuzz(i)
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 ==0:
        print('Fizz')
    elif i % 5 ==0: 
        print('Buzz')
print('please input 'FizzBuzz(i))