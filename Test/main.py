import random

# random_list = []
#
# for num in range(1, 10):
#     random_list += [random.randint(1, 10)]
# print(random_list)

# nums = [6, 3, 7, 2, 6, 4, 8, 9, 5]
# fruits = ["apple", "banana", "orange"]
# fruits.append("lime")
# fruits.extend(["grapy", "cherry"])
# print(nums[4])
# print(len(nums))
# print(fruits[2])
# print(fruits)
# print(len(fruits))
# print(len(fruits[4]))
# #fruits.extend(nums)
# print(fruits)
# #random.shuffle(fruits)
# fruits.sort(reverse = True)
# print(fruits)


# nums = [6, 3, 7, 2, 6, 4, 8, 9, 5]

# sum = 0
# for num in nums:
#     sum = num + sum
# print(sum)

# list = []
# sum = 0
# for i in range(30):
#     list.append(i**2)
#     sum += i
#     #list.sort(reverse=True)
#     len(list)
# print(list)
# print(len(list))
# print(sum)

name = "aruana garcia"
#print(type(name))
# list(name)
# type(list)
# list.remove(7)
# print(list(name))

#Exercício 01#

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(nums[1:10])
# print(nums[8:14])
# nums_even = []
# nums_odd = []
# mult_3 =[]
# mult_2 =[]
# mult_4 =[]
#
# for num in nums:
#     if num % 2 == 0:
#         nums_even.append(num)
#     else:
#         nums_odd.append(num)
# for num in nums:
#     if num % 2 == 0:
#         mult_2.append(num)
#     if num % 3 == 0:
#         mult_3.append(num)
#     if num % 4 == 0:
#         mult_4.append(num)
#
# sum1 = 0
# sum2 = 0
# for num in nums[10:]:
#     sum1 += num
# for num in nums[3: 10]:
#     sum2 += num
# sum = sum1 + sum2
#
# print(nums_even)
# print(nums_odd)
# print(mult_2)
# print(mult_3)
# print(mult_4)
# print(sorted(nums, reverse=True))
# print(sum)

#exercício02
# lista = [11, 12, 14, 13, 20]
# for i, p in enumerate(lista):
#     print(i + 1, '=>', p)
#
# #exercício03
# lista2 = [1.2, 2.3, 4.5, 10.3, 5.3]
# print(sorted(lista2, reverse=True))
#
# #exercício04
# notas = [9.0, 6.0, 10.0, 3.0]
# soma = 0
# for nota in notas:
#     soma += nota
# media = soma / len(notas)
# print(media)

#exercícios05
# notas = []
# for nota in range(10):
#     notas += [random.randint(1, 50)]
# print(notas)
# print(max(notas))
# print(min(notas))

#exercícios06
# nums = []
# nums_even = []
# nums_odd = []
# for num in range(20):
#     nums += [random.randint(1, 101)]
# for num in nums:
#     if num % 2 == 0:
#         nums_even.append(num)
#     else:
#         nums_odd.append(num)
# print(nums)
# print(nums_even)
# print(nums_odd)

#exercício07

# temps = []
# temps_above = []
# temps_under = []
# meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
# for temp in range(12):
#     temps += [round(random.uniform(12.0, 43.5),1)]
# print(temps)
# sum = 0
# for temp in temps:
#     sum += temp
# media = sum / 12
# for temp in temps:
#     if temp > media:
#         temps_above += [temp]
#     if temp < media:
#         temps_under += [temp]
#     for i in range(12):
#         if temp > media:
#             print(f"{meses[i]} : {temps[i]}")
#
# print(media)
# print(temps_above)
# print(temps_under)

#exercício08







