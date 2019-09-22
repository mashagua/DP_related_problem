# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:58:21 2019

@author: masha
"""

def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
import timeit
#根据传入的参数，对这个函数跑100次，
timeit.timeit('fib(10)',number=100,globals=globals())
timeit.timeit('fib(20)',number=100,globals=globals())
timeit.timeit('fib(30)',number=100,globals=globals())

def fib(n,cache=None):
    if n==0:
        return 1
    if n==1:
        return 1
    if cache is None:
        cache={}
    if n in cache:
        return cache[n]
    result=fib(n-1,cache)+fib(n-2,cache)
    cache[n]=result
    return result

timeit.timeit('fib(10)',number=100,globals=globals())
timeit.timeit('fib(20)',number=100,globals=globals())
timeit.timeit('fib(30)',number=100,globals=globals())
#
def fib(n):
    a=1
    b=1
    if n>=2:
        for i in range(2,n+1):
            a,b=b,a+b
    return b

timeit.timeit('fib(10)',number=100,globals=globals())
timeit.timeit('fib(20)',number=100,globals=globals())
timeit.timeit('fib(30)',number=100,globals=globals())
def house_robber(house_values):
    a=0
    b=0
    for val in house_values:
        a,b=b,max(b,a+val)
    return b

import math
def coins(denominations,target):
    cache={}
    def subproblem(i,t):
        if (i,t) in cache:
            return cache[(i,t)]
        val=denominations[i]
        if val>t:
            choice_take=math.inf
        elif val==t:
            choice_take=1
        else:
            choice_take=1+subproblem(i,t-val)
        choice_leave=(math.inf if i==0 else subproblem(i-1,t))
        optimal=min(choice_take,choice_leave)
        cache[(i,t)]=optimal
        return optimal
    return subproblem(len(denominations)-1,target)

coins([1,5,12,19],16)
timeit.timeit('coins([1,5,12,19],16)',number=100,globals=globals())
