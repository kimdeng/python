#!/usr/bin/python

#关键字参数调用

def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
    print "-- this parrot wouldn't",action,
    print "if you put",voltage,"volts throuhg it."
    print "--lovely plumage,the",type
    print "-- It's",state,"!"

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000,action='vooooom')
parrot(action='vooooom',voltage=1000000)
parrot('a million','bereft of life','jump')
parrot('a thousand',state='pushing up the daisies')
