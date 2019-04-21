class node(object):
    def __init__(self, x, y, g=None):
        self.xy = (x,y)
        self.g  = g


    def __eq__(self, other):
        if self.xy == other:
            return True
        else:
            return False


a = node(1,2,3)
b = node(1,2,5)
c = node(1,4,6)

x = [a,b,c]
t = node(6,4,1)

print(x.index(c))