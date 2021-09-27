# Условные операторы

var = 5

# if имеет условие
# выполянет код внутри тела, если условие истинно 
# if var != 0:
	# print('hello')

# if var < 0:
	# print('hello')

# var = -1

# if var < 0:
# 	print('меньше 0')
# else:
# 	print('не меньше 0')

var = 'A'

if var == 'A':
	res = 'lit A'
# else if = elif	
elif var == 'B':
	res = 'lit B'
elif var == 'C':
	res = 'lit C'
elif var == 'a':
	res = 'lit a'
else:
	res = 'не один из вариантов'

# print(res)


# Пример. 'Термостат'

# текущая температура
current_temp = int(input('t=',))

# диапазон температур
min_temp = 21
max_temp = 26

# логика термостата
if current_temp < min_temp:
	print('ON')
elif current_temp > max_temp:
	print('OFF')
else:
	print('Температура оптимальна')