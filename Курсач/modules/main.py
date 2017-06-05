from ADT import Array


def read_data():
    """reads data file"""
    data = {}
    for line in open('data.txt'):
        line = line.split('\n')  # from str into dict
        line = line[0]  # get rid of last element
        line = line.split(' ')  # divide the elements
        line[1] = str(line[1])  # making coords
        line[2] = str(line[2])
        data[line[0]] = line[1:]
    return data

def suggestion(data):
    """gives suggestions to buyer"""
    middle_price = 'from 5 to 18'
    high_price = 'from 18 to 50'
    cheap_price = 'to 5'
    if data['Role1'] == data['Role'] == data['Role2'] == data['Role3'] == data['Role4']:
        if 5 <= (data['ItemPrice_currencyID="USD"'][int(0)] + data['ItemPrice_currencyID="USD"1'][int(0)] +
                data['ItemPrice_currencyID="USD"2'][int(0)]) / 3 <= 18:
            print('Probably, the best option in price for you is: wares with middle price', middle_price)
        elif (data['ItemPrice_currencyID="USD"'][int(0)] + data['ItemPrice_currencyID="USD"1'][int(0)] +
                data['ItemPrice_currencyID="USD"2'][int(0)]) / 3 >= 18:
            print('Probably, the best option in price for you is: wares with higher price', high_price)
        else:
            print('Probably, the best option in price for you is: wares with cheaper price', cheap_price)
suggestion(read_data())

Array(len(read_data()))