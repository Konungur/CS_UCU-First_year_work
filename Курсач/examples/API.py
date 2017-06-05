data = {}
for line in open('data.txt'):
    line = line.split('\n')  # from str into dict
    line = line[0]  # get rid of last element
    line = line.split(' ')  # divide the elements
    line[1] = str(line[1])  # making coords
    line[2] = str(line[2])
    data[line[0]] = line[1:]
print(data)

