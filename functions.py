def send_data(data):
    array = []
    dictionary = {}
    for i in range(len(data)):
        dictionary = {'BankName': data[i][0], 'USDBuy': data[i][1], 'USDSell': data[i][2]}
        array.append(dictionary)
    test = array
    print(test)
    return test
