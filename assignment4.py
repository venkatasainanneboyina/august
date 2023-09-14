print('write a programm to get square of every element by using map fucntion')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=map(lambda n : n*n,l)
print(list(f))

print()
print()

print('write a programm to sum every number by 10')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=map(lambda n : n+10,l)
print(list(f))

print()
print()

print('write a programm to multiply every number by 2 ')
l=eval(input('enter a nums that you want in a single line sperated by comma(,): '))
f=map(lambda n : n*2,l)
print(list(f))

print('write a nested function to get sum and product of given numbers')
def fun1(x,y):
    print(f'sum = {x+y}')
    def pro(x,y):
        print(f'pro = {x*y}')
    pro(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun1(x,y)

print()
print()

print('write a nested function to get greater and lowest of given numbers')
def fun2(x,y):
    print(f'greater = {x if x>y else y}')
    def low(x,y):
        print(f'lowest = {x if x<y else y}')
    low(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun2(x,y)

print()
print()

print('write a nested function to get numbers multiplied by 10 and divided by 10 of given numbers')
def fun3(x,y):
    print(f'multiplied by 10 = {x*10,y*10}')
    def div(x,y):
        print(f'divided by 10 = {x/10,y/10}')
    div(x,y)

x=int(input('enter a number 1: '))
y=int(input('enter a number 2: '))
fun3(x,y)

from functools import*
print('write a programm to get sum of all the digits')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n+m,l)
print(f)

print()
print()

print('write a programm to get product of every element')
l=eval(input('enter a numbers that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n*m,l)
print(f)

print()
print()

print('write a programm to get highest element in a given elements ')
l=eval(input('enter a nums that you want in a single line sperated by comma(,): '))
f=reduce(lambda n,m : n if n>m else m,l)
print(f)
