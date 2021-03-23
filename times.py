from __future__ import absolute_import, unicode_literals
from __future__ import division, print_function
import datetime
import time
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

#North American Time Zones
GMT = Zone(0,False,'GMT')
AST = Zone(-4,False,'AST')
EST = Zone(-5,False,'EST')
CST = Zone(-6,False,'CST')
MST = Zone(-7,False,'MST')
PST = Zone(-8,True,'PST')
AKST = Zone(-9,True,'AKST')
HAST = Zone(-10,True,'HAST')

#European Time Zones
BST = Zone(+1,True,'BST')
CEST = Zone(+2,True,'CEST')
EEST = Zone(+3,True,'EEST')
MSK = Zone(+4,True,'MSK')

#Australian Time Zones
AEST = Zone(+10,True,'AEST')
AWDT = Zone(+9,True,'AWDT')
AWST = Zone(+8,True,'AWST')

#x = datetime.datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S %Z')
#b = datetime.datetime.now(GMT).strftime('%m/%d/%Y %H:%M:%S %Z')

#North American Time Zones
a = datetime.datetime.now(AST).strftime('%m/%d/%Y %H:%M:%S %Z')
b = datetime.datetime.now(EST).strftime('%m/%d/%Y %H:%M:%S %Z')
c = datetime.datetime.now(CST).strftime('%m/%d/%Y %H:%M:%S %Z')
d = datetime.datetime.now(MST).strftime('%m/%d/%Y %H:%M:%S %Z')
e = datetime.datetime.now(PST).strftime('%m/%d/%Y %H:%M:%S %Z')
f = datetime.datetime.now(AKST).strftime('%m/%d/%Y %H:%M:%S %Z')
g = datetime.datetime.now(HAST).strftime('%m/%d/%Y %H:%M:%S %Z')

#European Time Zones
aa = datetime.datetime.now(BST).strftime('%m/%d/%Y %H:%M:%S %Z')
bb = datetime.datetime.now(CEST).strftime('%m/%d/%Y %H:%M:%S %Z')
cc = datetime.datetime.now(EEST).strftime('%m/%d/%Y %H:%M:%S %Z')
dd = datetime.datetime.now(MSK).strftime('%m/%d/%Y %H:%M:%S %Z')