i = 0
j = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
k = ""
while i < 11:
    k = k + j[i]
    i = i + 1
    print(k)
else:
    print("Beyond Scope")
