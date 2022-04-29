def jsonattr(filepath):
    with open(filepath) as json_file:
        json_data = load(json_file)
        
    def wrapper(self):
        for k,v in json_data.items():
            setattr(self, k, v)
        return self
    return wrapper


@jsonattr('/tmp/myClass.json')
class MyClass:
    def __init__(self, foo, an_int, this_kata_is_awesome):
        self.foo = foo
        self.an_int = an_int
        self.this_kata_is_awesome = this_kata_is_awesome
        
if __name__ == '__main__':
    instance = MyClass('hello', 2, None)