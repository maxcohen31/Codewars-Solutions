class add(int):
    def __call__(self, number):
        return add(self + number)
    
s = add(1)(3)
print(s)    