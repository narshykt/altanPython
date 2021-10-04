# Циклы (операторы циклов)

# Оператор while

# бесконечный цикл (условие всегда True)
# while True: 
#     print("Hello")

# while с условием
num = 0
# while num < 10:
#     print(num)
#     # инкремент
#     # num = num + 1 длинная запись
#     num += 1 # короткая запись
#     print(num)

# прерывание цикла по дополнительному условию
num = 10

# while True:
#     if num == 5:
#         # break прерывает любой цикл
#         break
#     print(num)
#     # декремента 
#     num -= 1 

# while num < 100:
#     print("Python is good")
#     s = input("Введите команду: ")
#     if s == "stop":
#         print("Bye! bye!")
#         break
#     print(f"Вы ввели: {s}")
#     num += 30

# пропуск куска кода в теле цикла
# while True:
#     s = input("Вы робот:")
#     if s == "no":
#         print("красавчик")
#         continue
#     print("ха-ха")
#     break


#  Оператор for

# 1. читает элемент итерируемого объекта по порядку 
# 2. значение элемента присваивается в свою переменную 
# 3. выполянет блок кода своего тела

# for n in [1,2,3,4,5]:
#     print(n)

# for _ in (10,20,30,40):
#     print("Hello, World!")

# for char in "python":
#     print(char)

my_tuple = (10,20,30,40)

# for n in my_tuple:
#     res = n * 2
#     print(res)

# for n in my_tuple[::-1]:
#     res = n + 2
#     print(res)

# r = range(5,10)
# print(r)

# for i in range(5,10, 2):
#     print(i)

for i in range(10)[::-1]:
    print(i)

# генератор списка, кортежа, словаря