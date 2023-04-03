def SUCCESSIONAL_DIFFERENCE(variable_list):
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average= (1/delta_list[0])*SIGMA(OPERATE_VARIABLE_LIST(delta_list,lambda x:x/delta_list[0]))
    return average

def SIGMA(variable_list):
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    return sum

def OPERATE_VARIABLE_LIST(variable_list,operation):
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

def TRANSFORM_TO_DELTA(variable_list):
    for i in range(1,variable_list[0]//2+1):
        variable_list[i] = variable_list[i+variable_list[0]//2]-variable_list[i]
    variable_list[0]=variable_list[0]//2
    return variable_list

def LIST_AVERAGE(variable_list):
    sum = 0
    for i in range(1,variable_list[0]+1):
        sum += variable_list[i]
    average = sum / variable_list[0]
    return average

def UNCERTAINTY(variable_list,ub):
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average = LIST_AVERAGE(variable_list)
    delta_list = OPERATE_VARIABLE_LIST(delta_list,lambda x:(x-average)**2)
    ua=(SIGMA(delta_list)/delta_list[0])**0.5
    u = (ua**2+ub**2)**0.5
    return u


print(SUCCESSIONAL_DIFFERENCE(GET_VARIABLE_LIST()))
