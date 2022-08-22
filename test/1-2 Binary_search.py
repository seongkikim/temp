a = [5, 12, 28, 29, 40, 41, 53, 54, 68, 69, 79, 80, 83, 89, 90, 100]
x = input('숫자를 입력하시오: ')
left = 0
right = len(a) - 1
 
while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x): 
        print(' {:3}이(가) a[{:2}]에 있다.'.format(x, middle))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1
 
if left > right:
    print(' {:3}이(가) 배열에 없다.'.format(x))
