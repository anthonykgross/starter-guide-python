"""
COMMENT
"""
print("Hello world ! \n")

"""
BE CAREFUL : PYTHON IN TABBED SENSITIVE

EXAMPLE :

for i in range(0, 10):
print("%d" % i)

Won't works ! 
"""
print("Example : FOR")
for i in range(0, 10):
    print("%d" % i)

print("\nExample : WHILE")
i = 0
while i < 10:
    print("%d" % i)
    i += 1

print("\nExample : IF")
i = 0
if i >= 0:
    print("`i` is higher than or equals 0")

print("\nExample : IF ELSE")
if i > 0:
    print("`i` is higher than 0")
else:
    print("`i` is not higher than 0")

print("\nExample : LIST")
list = ['I','LOVE','PYTHON', '3']
for l in list:
    print("`l` is equals `%s`" % l)


print("\nExample : IMPORT")
from my_class import MyClass

print("\nExample : FUNCTION")
def my_function(i):
    return i*10;
print("Return : %d" % my_function(2))

print("\nExample : OOP")
cls = MyClass()
print(cls.attribute) # print("my_value")
# print(cls.__another_attribute) # ERROR : Private attribute

print("\nExample : ARGS")
cls.set("I", "LOVE", "PYTHON")

print("\nExample : KWARGS")
cls.set(value="I", param="LOVE", r="PYTHON")

print("\nExample : PARAM + ARGS")
cls.define("I", "LOVE", "PYTHON")


print("\nExample : OS")
import os
files = os.listdir(".")
for file in files:
    print("%s" % file)


print("\nExample : DATETIME")
import datetime
now = datetime.datetime.now()
print("%s" % now)
print("%s" % now.strftime("%Y-%m-%d %H:%M:%S"))

"""
ONLY FOR PYTHON 3 
"""
print("\nExample : PROMPT")
python = input('What do I love : ')
print(python)
