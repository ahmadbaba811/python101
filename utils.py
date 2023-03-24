def weight_converter(my_wieght) :
    weight_unit = input("(L) for pounds, (K) for kilogram ")
    weight_unit = weight_unit.lower()
    if weight_unit == "l" :
        converted_wieght = float(my_wieght) * 0.45
        print(converted_wieght)
    else:
        converted_wieght = float(my_wieght) / 0.45
        print(converted_wieght)


def find_maximum(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num