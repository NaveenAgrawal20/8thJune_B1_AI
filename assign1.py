Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20
>>> a += 30
>>> a %= 3
>>> print(a)
2
>>> True*False
0
>>> True & False
False
>>> True and False
False
>>> ((6 > 3) and (7 < 4) or (18 == 3)) and (9 >3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> s1+" "+s2
'Nice to have it here'
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2][0]
'hello'
>>> a = [s1]+a
>>> a += [s2]
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> print(color_list_1 - color_list_2)
{'White', 'Black'}
>>>len(set('abcdefghijklmnopqrstuvwxyz') - set(input("Enter str: ").lower())) == 0
Enter str: The quick brown fox jumps over the lazy dog
True
>>>eval('{0}+{0}{0}+{0}{0}{0}'.format(input("Enter a num")))
Enter a num5
615
>>> sorted(input("Enter strings ").split(","))
Enter strings without,hello,bag,world
['bag', 'hello', 'without', 'world']
>>> d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
>>> print(d['Student'][d['Marks'].index(max(d['Marks']))])
Kishore