from re import sub


"""
Если считан токен '(' - добавляем новый узел, как левого потомка текущего, и спускаемся к нему вниз.
Если считанный один из элементов списка ['+','-','/','*'], то устанавливаем корневое значение текущего узла
равным оператору из этого токена. Добавляем новый узел на место правого потомка текущего и спускаемся вниз по
правому поддереву.
Если считанный токен - число, то устанавливаем корневое значение равным этой величине и возвращаемся к родителю.
Если считан токен ')', то перемещаемся к родителю текущего узла.

"""



class Node:
    def __init__(self, right=None, left=None, token=None):
        self.right = right
        self.left = left
        self.token = token

    def compute(self):
        if self.left and self.right:
            return str(eval(self.left.compute() + self.token + self.right.compute()))
        else:
            return self.token


    def set_right(self, token=None):
        self.right = Node(token=token)
        return self.right

    def set_left(self, token=None):
        self.left = Node(token=token)
        return self.left



    def __str__(self):
        return '(%s %s %s)' % (self.left or '', self.token, self.right or '')


class Tree:
    def __init__(self, exp):
        assert type(exp) == str
        exp = sub(r'[()]', lambda p: ' ' + p.group(0) + ' ', exp)
        self.root = Node()
        self.build(exp)

    def build(self, exp):
        cur = self.root
        stack = []
        for i in exp.split():
            if i == '(':
                stack.append(cur)
                cur = cur.set_left()
            elif i.isdigit():
                cur.token = i
                cur = stack.pop()
            elif i in '-+*/':
                stack.append(cur)
                cur.token = i
                cur = cur.set_right()
            elif i == ')':
                cur = stack.pop() if stack else None

    def __str__(self):
        return str(self.root)

    def compute(self):
        return self.root.compute()

tree = Tree('((((10 - 100) + 2) * (4 / 2)) + 1000)')
print(tree)
print(tree.compute())