A=int(input())
B=int(input())
H=int(input())
if A<=B and H>A and H>B:
    print("Пересып")
elif A<=B and H<A and H<=B:
    print("Недосып")
else:
    print("Это нормально")