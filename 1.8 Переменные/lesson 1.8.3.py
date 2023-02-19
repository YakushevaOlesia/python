x=int(input())  # Дано минуты
h=int(input()) # Дано часов
m=int(input()) # Дано минут

o = h*60+m # Время СЕЙЧАС в минутах
p=x+o # в минутах спим
h1=p//60
m1=p-h1*60
print(h1)
print(m1)