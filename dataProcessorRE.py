#在这一个重构文件当中，variable_list仅用于保存实验的变量

def SUCCESSIONAL_DIFFERENCE(variable_list):
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average = (1/len(delta_list))*SIGMA(OPERATE_VARIABLE_LIST(delta_list,lambda x:x/len(delta_list)))
    return average

def SIGMA(variable_list):
    return sum(variable_list)

def OPERATE_VARIABLE_LIST(variable_list,opt):
    return [opt(each) for each in variable_list]

def GET_VARIABLE_LIST() -> list:
    variable_list = eval(input("Input variables, use a comma \',\' between variables."))
    return variable_list

def TRANSFORM_TO_DELTA(variable_list:list) -> list:
    l = len(variable_list)
    delta_list = [variable_list[i + l // 2] - variable_list[i] for i in range(l // 2 + 1)]
    return delta_list

#在原本的实现当中，你把python自己的sum函数给重定义了
def LIST_AVERAGE(variable_list):
    S = sum(variable_list)
    try:
        return S / len(variable_list)
    except ZeroDivisionError:
        print("Variable_list is empty!")

def UNCERTAINTY(variable_list,ub):
    delta_list = TRANSFORM_TO_DELTA(variable_list)
    average = LIST_AVERAGE(variable_list)
    delta_list = OPERATE_VARIABLE_LIST(delta_list,lambda x:(x-average)**2)
    ua=(SIGMA(delta_list)/len(delta_list))**0.5
    u = (ua**2+ub**2)**0.5
    return u


print(SUCCESSIONAL_DIFFERENCE(GET_VARIABLE_LIST()))