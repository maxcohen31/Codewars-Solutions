class Plugboard(object):
    def __init__(self, wires=''):
        """
        wires: This is the mapping of pairs of characters
        """
        if len(wires) > 20 or len(wires) % 2 != 0 or len(set(wires)) != len(wires):
            raise Exception('Too many wires defined')
        
        self.dict_to = {wires[idx]:wires[idx+1] for idx in range(0, len(wires), 2)}
        self.from_dict = {wires[idx+1]:wires[idx] for idx in range(0, len(wires[::-1]), 2)}                       
        
        
    def process(self, c):
        """
        c: The single character to process
        """
        if c in self.dict_to:
            c = self.dict_to[c]
        elif c in self.from_dict:
            c = self.from_dict[c]
        return c 
    
    
p = Plugboard('ABCD')
print(p.process('D'))

