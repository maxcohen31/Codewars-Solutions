def data_reverse(data):
    result = []
    splitted_list = [data[i:i+8] for i in range(0, len(data), 8)]
    for i in reversed(splitted_list):
        result.append(i)
    return [i for sub_data in result for i in sub_data]


data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print(data_reverse(data1))