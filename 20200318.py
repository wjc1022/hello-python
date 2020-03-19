# 定义一个带有3个参数函数
# 判断其是否能够组成一个三角形，可以返回true 不能返回false
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print('true')
    else:
        print('false')

triangle(1,2,1)

# def triangle(a,b,c):
#     if a+b>c：
#         continue
#     elif a+c>b:
#         continue
#     elif b+c>a：
#         print('true')
#     else:
#         print('false')
# triangle(1,2,1)



def qwq(a,b):
    if a < b:
        a, b = b, a
    while b > 1:
        if a % b == 0:
            break
        b = b - 1
    return b

result = qwq(6,9)
print(result)