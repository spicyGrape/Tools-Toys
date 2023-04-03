def SUCCESSIONAL_DIFFERENCE(variable_list:list):
    variable_num = len(variable_list)
    sum = 0
    for i in range(0,variable_num//2):
        sum -= variable_list[i]
        sum +=variable_list[variable_num-1-i]
    sum /= (variable_num//2)
    sum /= (variable_num//2)
    return sum

def GET_VARIABLE_LIST() -> list:
    variable_list = []
    variable_list = eval(input("Input variables, use a comma \',\' between values:"))
    
    return variable_list

#SUCCESSIONAL_DIFFERENCE(GET_VARIABLE_LIST())

variables = GET_VARIABLE_LIST()
print(SUCCESSIONAL_DIFFERENCE(variables))