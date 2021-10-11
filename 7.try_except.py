# Исключения (исключительные события, искл. ситуации, ошибки)

# Пример исключения при делении на ноль

# a = 100
# b = 10

# отлов исключения
# try:
#     # потенциально аварийный код
#     c = a / b
# except:
#     # код, который должен сработать при обноружении исключения (ошибки)
#     print("Error")
#     c = 0

# print(c)


# Обработка множества исключений
# try:
#     var_1 = int(input("Введите число: "))
#     result = 100 / var_1
# # Обработка конкретных исключений
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Нужно ввести число!")
# # обработка общего исключения
# except Exception as error:
#     print(error)


# Конструкция "try-except-else"

# try:
#     a = int(input("Введите число: "))
#     c = 100 / a
# except ZeroDivisionError:
#     c = 0 
# # блок else срабатывает если НЕ отлавливаются исключения
# else:
#     print(f'Result: {c}')

# Конструкция "try-except-finally"
# try:
#     a = int(input())
#     c = 100 / a
#     print("Correctly")
# except ZeroDivisionError:
#     c = 0
#     print("Error")
# finally:
#     print("finally")

# Кастомизированные исключения
try:
    a = int(input("Введите число: "))
    if a == 0:
        raise Exception("На ноль делить нельзя!")
    c = 100 / a
    print("Полет нормальный")
except Exception as err:
    print(err)

# Пример приближенный к реальности
while True:
    try:
        a = input("Введите число: ")
        # if isinstance(a, str):
        #     raise Exception("Нужно ввести число!")
        b = int(a)
        if b == 0:
            raise Exception("На ноль делить нельзя")
    except ValueError:
        print("Это не число!")
        continue
    except Exception as err:
        print(err)
        continue