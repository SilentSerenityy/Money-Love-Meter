from __future__ import absolute_import, unicode_literals
from __future__ import division, print_function
import datetime
import time

import randomclass Zone(datetime.tzinfo):
    def __init__(self,offset,isdst,name):
      self.offset = offset
      self.isdst = isdst
      self.name = name
    def utcoffset(self, dt):
      return datetime.timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
      return datetime.timedelta(hours=1) if self.isdst else datetime.timedelta(0)
    def tzname(self,dt):
      return self.name

EST = Zone(-5,False,'EST')
day = datetime.datetime.now(EST).strftime('%m/%d/%Y %H:%M:%S %Z')

while True:
    name = input("Your name: ")

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
    
    print("Thanks for the affection!")
