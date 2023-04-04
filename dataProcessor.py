# 原始数据的数据量必须为偶数


def succession_difference(variable_list: list) -> float:
    """
    对数列用逐差法求delta均值
    """
    delta_list = transform_to_delta(variable_list)
    average = (1 / delta_list[0]) * sigma(delta_list)
    return average


def sigma(variable_list):
    """
    求和数列
    """
    add_up = 0
    for i in range(1, variable_list[0] + 1):
        add_up += variable_list[i]
    return add_up


def operate_variable_list(variable_list, operation):
    """
    对数列每一位进行operation操作
    """
    operated_variable_list = [variable_list[0]]
    for i in range(1, variable_list[0] + 1):
        operated_variable_list.append(operation(variable_list[i]))
    return operated_variable_list


def get_variable_list():
    variable_list = [int(input('Type in the number of variables: '))]
    for i in range(1, variable_list[0] + 1):
        variable_list.append(float(input("Input the variables: ")))
        i += 1
    return variable_list


def transform_to_delta(variable_list: list) -> list:
    """
    逐差的delta平均值
    """
    transformed_list = [variable_list[0] // 2]
    for i in range(1, variable_list[0] // 2 + 1):
        transformed_list.append((variable_list[i + variable_list[0] // 2] - variable_list[i]) / (variable_list[0] // 2))
    return transformed_list


def list_average(variable_list):
    """
    传入需要求均值的数列
    """
    add_up = 0
    for i in range(1, variable_list[0] + 1):
        add_up += variable_list[i]
    average = add_up / variable_list[0]
    return average


def uncertainty(variable_list, ub):
    """
    传入未经处理的原始数据
    """
    delta_list = transform_to_delta(variable_list)

    average = succession_difference(variable_list)
    ua = (sigma(operate_variable_list(delta_list, lambda x: (x - average) ** 2)) / (delta_list[0] - 1)) ** 0.5
    u = (ua ** 2 + ub ** 2) ** 0.5
    return u


va_list = get_variable_list()
average_lambda = succession_difference(va_list)
u = uncertainty(va_list, 0)
print(average_lambda)
print(u)
