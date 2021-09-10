# Assume that the function will take in a list

def cal_sum(input:list) -> int:
    result:int = 0
    for item in input:
        if type(item) is int and 0 < item < 100 and item % 2 == 1:
            result += item
    return result


if __name__ == '__main__':
    test_input = [0, 24, 12, 324, 325, 12, 42, 23, 25]
    test_input_2 = [12, 'sd', 23, 123, 11, 23, 422, 11111, 23.423, '2344']
    result = cal_sum(test_input)
    result2 = cal_sum(test_input_2)
    print(result)
    print(result2)
