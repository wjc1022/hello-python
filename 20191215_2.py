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


    
for j in range(4):
    for i in range(4):
        if i-3+j<0:
            print(' ',end='')
        else:            
            print('*',end='')
    print()