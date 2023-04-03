def SUCCESSIONAL_DIFFERENCE():
    sum = 0
    variable_list=[]
    variable_num=int(input('The number of variables is:'))
    i = 1
    while i <= variable_num:
        variable_list.append(float(input("Input the variables:")))
        i += 1
    for i in range(0,variable_num//2):
        sum -= variable_list[i]
        sum +=variable_list[variable_num-1-i]
    print(sum)#test
    sum /= (variable_num//2)
    print(variable_num//2)#test
    sum /= (variable_num//2)
    return sum
print(SUCCESSIONAL_DIFFERENCE())