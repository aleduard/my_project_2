f = open('example.txt')

s = f.read(1)
print(s)
d = f.read(5)
print(d)
print(f.readline())
print(f.read())
f.close()

for line in open('example.txt'):
    if '3 lines' in line:
        print(line)


for line in open('data.txt')
    x = line.strip()
    print(x)