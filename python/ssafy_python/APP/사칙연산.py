class fourCal:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        result = self.x + self.y
        return result

a = fourCal(5,6)
print(a.add())