import os

x = os.getcwd()
print(x)

y = os.chdir(os.pardir)
print(os.getcwd())


os.chdir(x)

print(os.getcwd())


f = open('data.txt', 'rb')
s = f.read()
print(s, type(s))
print(str(s), type(str(s)))
f.close()
