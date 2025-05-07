

a = [30, 12, 21, 123, 42]
print(len(a))
i = 0
while i < len(a):
    a[i] = i
    i+=1
print(a) # [0, 1, 2, 3, 4]

i = 0
while i < len(a):
    a[i] = a[i] + 1
    i+=1
print(a) # [1, 2,3,4,5]

