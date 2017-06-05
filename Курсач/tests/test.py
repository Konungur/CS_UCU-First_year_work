data = {}
for line in open('data.txt'):
    line = line.split('\n')  # from str into dict
    line = line[0]  # get rid of last element
    line = line.split(' ')  # divide the elements
    line[1] = (line[1])  # making coords
    line[2] = (line[2])
    data[line[0]] = line[1:]
print(data)
print(" ")
print(" ")
print(" ")
v = '123'
y = int(v)
s = data['ItemPrice_currencyID="USD"'][int(0)]
b = data['ItemPrice_currencyID="USD"1'][int(0)] 
a = data['ItemPrice_currencyID="USD"2'][int(0)]
print(type(s))
print(b)
print(a)
print(type(v))
print(type(y))