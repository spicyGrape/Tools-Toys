#原始数据的数据量必须为偶数
def SUCCESSIONAL_DIFFERENCE(variable_list):#对数列用逐差法求delta均值
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average= (1/delta_list[0])*SIGMA(delta_list)
    return average

def SIGMA(variable_list):#求和数列
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    return sum

def OPERATE_VARIABLE_LIST(variable_list,operation):#对数列每一位进行operation操作
    operated_variable_list = [variable_list[0]]
    for i in range(1,variable_list[0]+1):
        operated_variable_list.append(operation(variable_list[i]))
    return operated_variable_list

def GET_VARIABLE_LIST():
    variable_list = []#0号存放变量个数，1~n存放变量
    variable_list.append(int(input('Type in the number of variables: ')))
    for i in range(1,variable_list[0]+1):
        variable_list.append(float(input("Input the variables: ")))
        i += 1
    return variable_list

def TRANSFORM_TO_DELTA(variable_list):#逐差的delta平均值
    transformed_list = [variable_list[0]//2]
    for i in range(1,variable_list[0]//2+1):
        transformed_list.append ((variable_list[i+variable_list[0]//2]-variable_list[i])/(variable_list[0]//2))
    return transformed_list

def LIST_AVERAGE(variable_list):#传入需要求均值的数列
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    average = sum / variable_list[0]
    return average

def UNCERTAINTY(variable_list,ub):#传入未经处理的原始数据
    delta_list = TRANSFORM_TO_DELTA(variable_list)

    average = SUCCESSIONAL_DIFFERENCE(variable_list)
    ua=(SIGMA(OPERATE_VARIABLE_LIST(delta_list,lambda x:(x-average)**2))/(delta_list[0]-1))**0.5
    u = (ua**2+ub**2)**0.5
    return u


va_list = OPERATE_VARIABLE_LIST(GET_VARIABLE_LIST(),lambda x:x*2)
average_lambda =SUCCESSIONAL_DIFFERENCE(va_list)
uncertainty = UNCERTAINTY(va_list,0.005)
print(average_lambda*37.580)
print(uncertainty*37.580)