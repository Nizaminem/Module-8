

def personal_sum(numbers): #если передавать параметр через (*numbers), то функция неправильно работает, так как функция раскрывает кортеж в виде отдельных переменных.
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            if isinstance(i, bool):
                raise TypeError ("Логические значения не учитываются")
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):

    if isinstance(numbers, int):
        return None
    try:
        res_per_sum = personal_sum(numbers)
        return res_per_sum[0] / (len(numbers) - res_per_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записаен некорректный тип данынх'



print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')