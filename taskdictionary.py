print('1.Write a Python script to add a key to a dictionary.')
d={1: 10, 2: 20}
key=input('enter a key to add: ')
value=input('enter a value to add: ')
d[key]=value
print(d)

print()
print()

print('2.Write a Python script to check whether a given key already exists in a dictionary.')
d={'a': 10, 'b': 20, 'c':30}
key=input('enter a key to check: ')
if d.get(key) == None:
    print('Given key is not in dictnoary')
else:
    print('given key is in dictonary')

print()
print()

print('3.Write a Python program to iterate over dictionaries using for loops')
d={'a': 10, 'b': 20, 'c':30}
for items in d.items():
    print(items)

print()
print()

print('4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.')
d={}
for i in range(1,13):
    d[i]=i*i
print(d)

print()
print()

print('5.Write a Python program to create a dictionary from a string.')
s=input('enter a string: ')
s=s.replace(' ','')
d={}
for NV in s:
    d[NV]=s.count(NV)
print(d)

print()
print()

print('6. Write a Python program to sum all the items in a dictionary.')
d={'a': 30, 'b': 20, 'd':40}
sum=()
for i in d.items():
    sum+=i
print(sum)

print()
print()

print('7.Write a Python program to combine two dictionary by adding values for common keys.')
d1 = {'a': 10, 'b': 20, 'c':30}
d2 = {'a': 30, 'b': 20, 'd':40}
for key in d1.keys():
    if key in d2.keys():
        d2[key]=d1.get(key)+d2.get(key)
    else:
        d2[key]=d1.get(key)
print(d2)

print()
print()

print('8.Write a Python program to access dictionary keys element by index.')
d={'physics': 36, 'math': 77, 'chemistry':92}
print(d.items())
index=int(input('enter a index position from 0 to 2: '))
print(list(d.keys())[index])

print()
print()

print('9.Write a Python program to remove a key from a dictionary.')
d = {'a': 10, 'b': 20, 'c':30}
print(d)
key=input('enter a key to remove: ')
d.pop(key)
print(d)

print()
print()

print('10.Write a Python script to merge two Python dictionaries.d')
d1={'a': 30, 'b': 20, 'd':40}
d2={'e': 10, 'f': 20, 'c':30}
print(d1)
print(d2)
d1.update(d2)
print(d1)