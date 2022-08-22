a = [5, 7, 3, 4, 8, 1, 9, 0, 2, 6]
x = a[0]
for i in range(len(a)):
    if a[i] > x: 
        x = i
print('최대 숫자는 a[', x, '] =', a[x])
