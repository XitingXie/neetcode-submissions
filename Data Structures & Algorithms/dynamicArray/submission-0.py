class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * self.capacity
        self.last_element_pos = -1

    def get(self, i: int) -> int:
        print(self.array)
        if i<0 or i>self.last_element_pos:
            return None
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i<0 or i>self.last_element_pos:
            return
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.last_element_pos == self.capacity - 1:
            self.resize()
        self.last_element_pos += 1
        self.array[self.last_element_pos] = n

    def popback(self) -> int:
        if self.last_element_pos == -1:
            return None
        else:
            self.last_element_pos-=1
            return self.array[self.last_element_pos+1]
 
    def resize(self) -> None:
        old_array = self.array
        self.capacity = 2 * self.capacity
        self.array = [0] * self.capacity
        for i in range(len(old_array)):
            self.array[i] = old_array[i] 
        self.last_element_pos = len(old_array)-1

    def getSize(self) -> int:
        return self.last_element_pos+1

    def getCapacity(self) -> int:
        return self.capacity
