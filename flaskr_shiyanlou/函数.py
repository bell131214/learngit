#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def add(a=2,b=19):
#     return a+b
# print add()
# print add(4,9)


class A(object):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b


class B(A):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def sub(self):
        return self.a - self.b


count = A(5,10)# 实例化
count1 =B(5,6)

print count1.add()

