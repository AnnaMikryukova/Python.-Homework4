# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите число: "))
i = 2 
my_list = []
num1 = N
while i <= N:
	if N % i == 0:
		my_list.append(i)
		N //= i
		i = 2
	else:
		i += 1
print(f"Простые множители числа {num1} = {my_list}")
