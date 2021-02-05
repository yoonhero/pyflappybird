import math

prime_list = [2]
def prime(list):
    condition = False
    for i in range(3, 10000):
        length = len(list)
        condition = False
        for j in range(0, length):
            if i % list[j] == 0:
                #no code
                condition = True
        if condition == False:
            list.append(i)

    return list

def mersen (list):
    mersen_num = 0
    num = []
    for i in range(1, 30):
        mersen_num = 2 ** i - 1
        if mersen_num in list:
            num.append(mersen_num)
    return print(num)


prime_list = prime(prime_list)
#mersen(prime_list)

