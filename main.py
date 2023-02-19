# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print (students)

# a = [1, 2, 3]
# b = a
# a[1] = 10
# b[0] = 20
# a = [5, 6]
# print(b)

# a=[int (i) for i in input().split()]
# print (a[0]+a[1]+a[2]+a[3])
#
#
# a = [ int(i) for i in input().split()]
#
#
# summ = 0
# l = len(a)
# for i in range(0,l):
#     summ = summ + a[i]
# print(summ)


s = [1, 1, 1, 1, 1, 2, 2, 2]
# s = [int(i) for i in input().split()]
s.sort()
res = s
for i in range(0, len(s) - 1):
    if s[i] != s[i + 1]:
        res.remove(s[i])
        print(res)

# новые данные
# рпоп
print(s)