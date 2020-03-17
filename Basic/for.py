for i in range(1,11):
    if i % 2 == 0:
        continue
    elif i % 5 == 0:
        pass
        # break
    else:
        print(i)
else:
    print("!! %d" % i)