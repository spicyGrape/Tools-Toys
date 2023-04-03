def SUCCESSIONAL_DIFFERENCE(variable_num,variable_list):
    sum = 0
    
    for i in range(0,variable_num//2):
        sum -= variable_list[i]
        sum +=variable_list[variable_num-1-i]
    sum /= (variable_num//2)
    sum /= (variable_num//2)
    return sum
def GET_VARIABLE_LIST():
    variable_num=int(input('Type in the number of variables: '))
    variable_list = []
    for i in range(variable_num):
        variable_list.append(float(input("Input the variables: ")))
        i += 1
    return variable_num,variable_list
#SUCCESSIONAL_DIFFERENCE(GET_VARIABLE_LIST())
a,b=GET_VARIABLE_LIST()
print(SUCCESSIONAL_DIFFERENCE(a,b))