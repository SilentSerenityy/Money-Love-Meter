import random
import times
from datetime import *
day = times.b


while True:
    name = input("Name: ")

    a = "💖 🖤 🖤 🖤 🖤 🖤 🖤 🖤 🖤 🖤"
    b = "💖 💖 🖤 🖤 🖤 🖤 🖤 🖤 🖤 🖤"
    c = "💖 💖 💖 🖤 🖤 🖤 🖤 🖤 🖤 🖤"
    d = "💖 💖 💖 💖 🖤 🖤 🖤 🖤 🖤 🖤"
    e = "💖 💖 💖 💖 💖 🖤 🖤 🖤 🖤 🖤"
    f = "💖 💖 💖 💖 💖 💖 🖤 🖤 🖤 🖤"
    g = "💖 💖 💖 💖 💖 💖 💖 🖤 🖤 🖤"
    h = "💖 💖 💖 💖 💖 💖 💖 💖 🖤 🖤"
    i = "💖 💖 💖 💖 💖 💖 💖 💖 💖 🖤"
    j = "💖 💖 💖 💖 💖 💖 💖 💖 💖 💖"

    x = [a, b, c, d, e, f, g, h, i, j]
    y = random.choice(x)

    if y == a:
      z = random.randint(50 , 55)
    elif y == b:
      z = random.randint(56 , 60)
    elif y == c:
      z = random.randint(61 , 65)
    elif y == d:
      z = random.randint(66 , 70)
    elif y == e:
      z = random.randint(71 , 75)
    elif y == f:
      z = random.randint(76 , 80)
    elif y == g:
      z = random.randint(81 , 85)
    elif y == h:
      z = random.randint(86 , 90)
    elif y == i:
      z = random.randint(91 , 95)
    elif y == j:
      z = random.randint(96 , 100)

    xx = str(day)
    yy = str(y)
    zz = str(z)

    xxx = f'Time: {xx}\n'
    yyy = f'Love Meter: {yy}\n'
    zzz = f'Coins Recieved: {zz}\n\n'

    r = open((name)+".txt","a")
    r.write(xxx)
    r = open((name)+".txt","a")
    r.write(yyy)
    r = open((name)+".txt","a")
    r.write(zzz)
    r.close()

    print(xxx, yyy, zzz)

