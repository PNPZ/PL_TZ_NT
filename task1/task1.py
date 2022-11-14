
n = int(input())
m = int(input())

array_one = m * [int(a) for a in range(1, n + 1) ]
array_two = ['']
array_3 = []
cnt = 0 

while array_two[-1] != 1:
    array_two.clear()
    for a in range(cnt, m + cnt):
        array_two.append(array_one[a])
        cnt += 1
    array_two_copy = array_two.copy()
    array_3.append(array_two_copy)
    cnt -= 1
for b in range(len(array_3)):
    print(array_3[b][0], end='')
