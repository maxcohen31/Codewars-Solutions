class Dinglemouse(object):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        if self.first_name == '':
            return self.last_name
        elif self.last_name == '':
            return self.first_name
        return self.first_name + ' ' + self.last_name
