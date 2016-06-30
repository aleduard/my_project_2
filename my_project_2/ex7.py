#f = open('data.txt')

def file_stats('data.txt')
input = open('data.txt')
l = ''
for line in open('data.txt'):
    if len(line) > len(l):
        l = line

        print('#=', len(l))

