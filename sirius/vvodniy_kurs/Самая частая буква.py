a = input().upper()
c = 0
l = ''
for i in a:
    if i.isalpha():
        if a.count(i) > c:
            l = '' + i
            c = a.count(i)
        elif a.count(i) == c and not(i in l):
            l += i
print(*sorted(l), sep='')
print(c)