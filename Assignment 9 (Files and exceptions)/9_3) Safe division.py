def divide_safe(num1_str, num2_str):
    try:
        num1_float = float(num1_str)
        num2_float = float(num2_str)
        result = num1_float / num2_float
        result = round(result, 5)
        return result
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

num1_str = input('Input first number: ')
num2_str = input('Input second number: ')

result = divide_safe(num1_str, num2_str)
print(result)