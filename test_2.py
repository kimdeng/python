#/usr/bin/python
#coding:utf-8


import string

def std_solution(text):

    table = string.maketrans(
            string.ascii_lowercase,
            string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    print string.translate(text,table)


text = 'map'

if __name__ == '__main__':

    std_solution(text)
