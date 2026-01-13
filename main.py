# ISDISJOINT
class MySet:
    def __init__(self):
        self.data = []

    def isdisjoint(self, other):
        for item in self.data:
            if item in other.data:
                return False
        return True

    def show(self):
        print(self.data)

s1 = MySet()
s1.data = [1, 2, 3]

s2 = MySet()
s2.data = [4, 5, 6]

print(s1.isdisjoint(s2))  
