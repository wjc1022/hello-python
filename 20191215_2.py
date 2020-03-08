# 输出以下图样
'''
*
**
***
****
'''

# for i in range(4):
#     for j in range(i+1):
#         print('*',end='')
#     print()

'''
   *
  **
 ***
****
'''


# for i in range(4):
#     for j in range(i):
#         if j-3<0:
#             print('1',end)
#         else:
#             print('*')


# for i in range(4):
#     if i-3<0:
#          print('1',end='')
#     else:            
#         print('*',end='')
# print()

# for i in range(4):
#     if i-2<0:
#         print('1',end='')
#     else:
#         print('*',end='')  
# print()     

# for i in range(4):
#     if i-1<0:
#         print('1',end='')
#     else:
#         print('*',end='') 
# print() 

# for i in range(4):
#     if i-0<0:
#         print('1',end='')
#     else:
#         print('*',end='')       

# for j in (3,2,1,0):
#     for i in range(4):
#         if i-j<0:
#             print('1',end='')
#         else:            
#             print('*',end='')
#     print()

    
for j in range(4):
    for i in range(4):
        if i-3+j<0:
            print(' ',end='')
        else:            
            print('*',end='')
    print()