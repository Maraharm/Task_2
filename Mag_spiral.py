"""Напишите программу, которая:
считывает одно число N, где 4<=N<=1000;
выводит на экран “магическую спираль” (матрицу размером n×n с числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке).
Пример:
$ python3 magic.py
4
1  2  3  4
12 13 14 5
11 16 15 6
10  9  8 7"""
def spiral():
    try:
        n = int(input())
        i, j = 0, -1
        max_j, max_i = n - 1, n - 1
        min_j, min_i = 0, 1
        count = 1
        mtrx = [[0 for j in range(n)] for i in range(n)]
        while True:

            while j < max_j:
                j += 1
                mtrx[i][j] = count
                count += 1
            max_j -= 1
            while i < max_i:
                i += 1
                mtrx[i][j] = count
                count += 1
            max_i -= 1
            while j > min_j:
                j -= 1
                mtrx[i][j] = count
                count += 1
            min_j += 1
            while i > min_i:
                i -= 1
                mtrx[i][j] = count
                count += 1
            min_i += 1

            if j == (n - 1) // 2 and i == n // 2:
                break

        print()
        print()
        for i in range(n):
            for j in range(n):
                print(mtrx[i][j], end=' ')
            print()
    except ValueError:
        print('ito ne celoe chislo')

spiral()
