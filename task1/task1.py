
n = int(input())
m = int(input())

array_1 = m * [int(a) for a in range(1, n + 1) ]
array_2 = ['']
array_3 = []
cnt = 0 

while array_2[-1] != 1:
    array_2.clear()
    for a in range(cnt, m + cnt):
        array_2.append(array_1[a])
        cnt += 1
    array_2_copy = array_2.copy()
    array_3.append(array_2_copy)
    cnt -= 1
for k in range(len(array_3)):
    print(array_3[k][0], end='')
