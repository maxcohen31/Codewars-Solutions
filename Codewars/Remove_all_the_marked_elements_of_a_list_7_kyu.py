class List:
    def remove_(self, integer_list, values_list):
        result = []
        for i in integer_list:
            if i not in values_list:
                result.append(i)
        return result

c = List()
print(c.remove_([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]))