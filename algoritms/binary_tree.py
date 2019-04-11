
class node:
    def __init__(self, value, right=None, left=None):
        self.right = right
        self.left = left
        self.value = value

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def set(self, value):
        if self.value == value:
            return
        if self.value > value:
            if not self.left:
                self.left = node(value)
            else:
                self.left.set(value)
        elif self.value < value:
            if not self.right:
                self.right = node(value)
            else:
                self.right.set(value)

    def __str__(self):
        return '(%s:%s:%s)' % (str(self.left or '*'), self.value, str(self.right or '*'))

class tree(node):
    def __init__(self, value=0):
        super().__init__(value)


    def set(self, value):
        super().set(value)



class dispatch:
    pass



tree = tree(50)


import random
for i in range(100):
    tree.set(random.randrange(100))
print(tree)
for i in tree:
    print(i)