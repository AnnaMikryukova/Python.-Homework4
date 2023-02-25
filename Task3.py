# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = list(map(int, input('Введите числа через пробел: ').split()))
new_list = []

for i in my_list:
	if i not in new_list:
		new_list.append(i)
print(f'->: {new_list}')
