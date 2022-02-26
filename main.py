from math import *

# task_1
print('task_1')

x = float(input('Введіть дійсне число x: '))

if 0 < x < 10:
    y = sqrt(x + 12)
else:
    y = 1 - tan(abs(x - 15))

print('y = ', y)


# task_2
print('\ntask_2')

x = float(input('Введіть дійсне число x: '))

if x < -20:
    y = x ** 2
elif x > 20:
    y = abs(cos(3 * x) + x / 2)
else:
    y = abs(3 * x ** 3)

print('y = ', y)

# task_3
print('\ntask_3')

x = float(input('Введіть перше дійсне число: '))
y = float(input('Введіть друге дійсне число: '))
z = float(input('Введіть третє дійсне число: '))

if x > (y and z):
    print('Перше число найбільше')
if y > (x and z):
    print('Друге число найбільше')
if z > (y and x):
    print('Третє число найбільше')

# task_4
print('\ntask_4')

x = float(input('Введіть дійсне число: '))

if x < -5:
    print('y = ', x ** 2)
elif x > 10:
    print('y = ', abs(cos(3 * x) + x / 2))
    print('z = ', tan(x))
else:
    print('y = ', abs(x+5) ** (1/5))
