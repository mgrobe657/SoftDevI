import arrays
class Queue:
    __slots__ = ['_front','_back','_size','_array']
    def __init__ (self,capacity = 3):
        self._array=arrays.Array(capacity)
        self._front=0
        self._back=0
        self._size=0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size
    
    def __repr__(self):
        string=''
        i = self._front
        while i != self._back:
            string += str(self._array[i])+', '
            i = (i + 1) % len(self._array)
        return '[' + string [:-2] + ']'
    
    def enqueue(self,value):
        self._array[self._back] = value
        self._back = (self._back + 1) % len(self._array)
        self._size += 1
        if self._back == self._front:
            self._resize()

    def get_front(self):
        return self._array[self._front]

    def get_back(self):
        return self._array[self._back-1]

    def dequeue(self,value):
        pass
    
    def main():
        new_q = Queue(3)
        print(new_q)
