class Genie():
    _all = ['Robin', 'Jonathan', 'Christian', 'Jean'] 

   
    @classmethod 
    def add_end(cls, ending): 
        return [name + ending for name in cls._all]
    
    @staticmethod
    def about():
        return 'This calls on the entire class, takes no arguments'


# Usage
print(Genie.add_end('aki')) #=> ['Jonathan', 'Jeannie']
print(Genie.about())
