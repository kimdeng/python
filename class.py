#!/usr/bin/python

class animals:
    def gou(self):
        print 'wangwangwang'
    def mao(self):
        print 'miaoiaomiao'

class gougou(animals):
    def gou(self):
        print 'wanwgwang'

class maomao(animals):
    def mao(self):
        print 'miaomiao'

x=animals()
x.gou()
x.mao()

y=gougou()
y.gou()

z=maomao()
z.mao()

