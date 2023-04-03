#原始数据的数据量必须为偶数
def SUCCESSIONAL_DIFFERENCE(variable_list):#对数列用逐差法求delta均值
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average= (1/delta_list[0])*SIGMA(OPERATE_VARIABLE_LIST(delta_list,lambda x:x/delta_list[0]))
    return average

def SIGMA(variable_list):#求和数列
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    return sum

def OPERATE_VARIABLE_LIST(variable_list,operation):#对数列每一位进行operation操作
    for i in range(1,variable_list[0]+1):
        variable_list[i]=operation(variable_list[i])
    return variable_list

def GET_VARIABLE_LIST():
    variable_list = []#0号存放变量个数，1~n存放变量
    variable_list.append(int(input('Type in the number of variables: ')))
    for i in range(1,variable_list[0]+1):
        variable_list.append(float(input("Input the variables: ")))
        i += 1
    return variable_list

def TRANSFORM_TO_DELTA(variable_list):#数列后一半减前一半
    for i in range(1,variable_list[0]//2+1):
        variable_list[i] = variable_list[i+variable_list[0]//2]-variable_list[i]
    variable_list[0]=variable_list[0]//2
    return variable_list

def LIST_AVERAGE(variable_list):#传入需要求均值的数列
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    average = sum / variable_list[0]
    return average

def UNCERTAINTY(variable_list,ub):#传入未经处理的原始数据
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average = LIST_AVERAGE(variable_list)
    delta_list = OPERATE_VARIABLE_LIST(delta_list,lambda x:(x-average)**2)
    ua=(SIGMA(delta_list)/delta_list[0])**0.5
    u = (ua**2+ub**2)**0.5
    return u


va_list = GET_VARIABLE_LIST()
average_lambda = 2 * SUCCESSIONAL_DIFFERENCE(va_list)
uncertainty = UNCERTAINTY(OPERATE_VARIABLE_LIST(va_list,lambda x: x*2),0.005)
print(average_lambda)
print(uncertainty)