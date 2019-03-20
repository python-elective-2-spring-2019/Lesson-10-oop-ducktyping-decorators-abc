
class A:
    """
        This is the constructor
    """
    
    def __init__(self, name):
        self.name = name

    # length
    def __len__(self):
        return 1234
    
    
    # Tostring
    def __str__(self):
        return self.name



a = A('Claus')

print(a)
#print(len(a))
print(sorted(A.__dict__))