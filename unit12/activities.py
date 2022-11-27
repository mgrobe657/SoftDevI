class Stack:
    __slots__ = ['_size','_is_empty']
    def __init__(self,size):
        self._size = size
        self._is_empty = True
    def is_empty(self):
        if self._size == 0:
            self._is_empty = True
        else:
            self._is_empty = False

def _stringify(self,node):
    if node == None:
        return ''
    else:
        return self._stringify(node.get_next()) + str (node.get_value())+ ', '

def __repr__(self):
    string = self._stringify(self._top)
    return '[' + string[:-2] + ']'

def push(self,value):
    new_node = node.Node(value,self._top)
    self._top = new_node
    self._size += 1

def peek(self):
    return self._top.get_value()

def pop(self):
    value = self._top.get_value()
    self._top = self._top.get_next()
    self._size -= 1
    return value

def main():
    # a_stack = Stack()
    # print(a_stack.is_empty())
    # a_stack.push('a')
    # a_stack.push('b')
    # a_stack.push('c')
    # print(repr(a_stack))
    pass
