from __future__ import absolute_import, unicode_literals
from __future__ import division, print_function
import datetime
import time
from tkinter import *
import tkinter.messagebox as box
import random

class Zone(datetime.tzinfo):
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

def moneylovemeter():
  import tkinter as tk

  def lovemeter():
    name = nameentry.get()

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

    day = datetime.datetime.now(EST).strftime('%m/%d/%Y %H:%M:%S %Z')
    xx = str(day)
    yy = str(y)
    zz = str(z)

    xxx = f'{xx}\n'
    yyy = f'I loved it this much!\n{yy}\n'
    zzz = f'I give you {zz} golden coins!'

    logx = f'Time: {xx}\n'
    logy = f'Love Meter: {yy}\n'
    logz = f'Coins Recieved: {zz}\n\n'

    r = open((name)+".txt","a")
    r.write(logx)
    r = open((name)+".txt","a")
    r.write(logy)
    r = open((name)+".txt","a")
    r.write(logz)
    r.close()

    box.showinfo(f"Thanks for snuggling me {name}!", \
    f"{xxx}{yyy}{zzz}")


  mlmeter = Tk()

  mlmeter.title("Snuggle Me!")

  mlwindow = Frame(master=mlmeter)

  nameentry = Entry(master=mlwindow, width=10)

  mlname = Label(master=mlwindow, text="Your name:")

  nameentry.grid(row=0, column=1, sticky="e")

  mlname.grid(row=0, column=0, sticky="w")

  snuggle = Button(master=mlmeter, text="Snuggle!", command=lovemeter)

  result = Label(master=mlmeter)

  mlwindow.grid(row=0, column=0)
  snuggle.grid(row=0, column=1)
  result.grid(row=2, column=0)


  mlmeter.mainloop()

moneylovemeter()
