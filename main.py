import matplotlib.pyplot as plt
import numpy as np
import math
import random as rnd

'''
# Блок инициализации переменных
amount = input()   # количество точек
p = input()        # длина окна
m = input()        # количество эпох обучения
nu = input()       # коэффициент обучения
'''

# Блок инициализации констант
amount = 20  # количество точек
p = 5  # длина окна
m = 30  # количество эпох обучения
nu = 1  # коэффициент обучения

# Блок задает значения интервала.
# [a:b] - начальный интервал функции
# [b:c] - прогнозируемый интервал функции
a = 1.7
b = 2.0
c = 2 * b - a
mo = 0  # матожидание ряда


# Заданная функция
def func(t):
    return math.sqrt(math.tan(-t))


# Построение графика по начальному интервалу
def start_chart(a, c, amount, mo):
    x_arr = list()
    y_arr = list()
    step = (b - a) / amount
    val = a
    for i in range(amount + 1):
        x_arr.append(val)
        val += step
    for i in range(amount + 1):
        y_arr.append(func(x_arr[i]))

    plt.plot(x_arr, y_arr, 'k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title('Start chart')
    plt.savefig('start_chart.png')

    return x_arr, y_arr


# Инициализация и обучение НС
def education(x_arr, amount, p, m, nu, mo):
    mass = np.zeros((p, amount - p))
    mo = 0
    for b in range(amount):
        mo += func(x_arr[b])
    for i in range(p):
        for k in range(amount - p):
            mass[i, k] = func(x_arr[i + k])

        print(mass[i])
    mo = mo / 20
    print('mo ', mo)

    w = np.zeros((p + 1))
    for i in range(p + 1):
        w[i] = rnd.randint(0, 2)
    print('w0: ', w)
    epochs = 0

    while epochs != m:
        epochs += 1
        print('epo ', epochs)
        e = 0
        for i in range(len(mass[0])):
            net = 0
            for j in range(p):
                net += w[j] * mass[j, i]
            net += mo
            print('net ', net)
            if i == (len(mass[0]) - 1):
                t = func(b + (b - a) / amount)
            else:
                t = mass[p - 1, i + 1]
            delta = t - net
            print('del ', delta)
            e += delta ** 2
            if delta != 0:
                for k in range(p):
                    w[k] += nu * delta * mass[k, i]
                w[p] += nu * delta
            print('  w ', w)
            print(' ')
        e = math.sqrt(abs(e))
        print('СК ошибка ', e)

    return w


#
#
# # Блок прогнозирования неизвестных значений
# def vanga(w, b, c, amount, p, points):
#
#     xv_arr = list()
#     step = abs(a - b) / amount
#     val = b
#     for i in range(amount + 1):
#         xv_arr.append(val)
#         val += step
#
#     yv_arr = list()
#     for i in range(amount+1):
#         val = 0
#         for k in range(p):
#             val += w[k]*points[k]
#         val+=w[4]
#         yv_arr.append(val)
#         points.pop(0)
#         points.append(val)
#
#     return xv_arr, yv_arr


# Результатирующий график
def fin_chart(a, c, xv_arr, yv_arr):
    x_arr = list()
    y_arr = list()
    step = (c - a) / amount * 2
    val = a
    for i in range(amount + 1):
        x_arr.append(val)
        val += step
    for i in range(amount + 1):
        y_arr.append(func(x_arr[i]))

    plt.plot(x_arr, y_arr, 'k', xv_arr, yv_arr, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title('Finish chart')
    plt.savefig('fin_chart.png')


x_arr, y_arr = start_chart(a, c, amount, mo)
w = education(x_arr, amount, p, m, nu, mo)
points = y_arr[amount - p:amount]
# xv_arr, yv_arr = vanga(w, b, c, amount, p, points)
# fin_chart(a, c, xv_arr, yv_arr)
