
class HashTable:

    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0 
        for elem in key:
            h += ord(elem)
        return h % self.MAX
    
    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __delitem__(self,index):
        h = self.get_hash(index)
        self.arr[h] = None


some_dict = HashTable()
some_dict['first'] = "Larry Page"
some_dict['second'] = "Sergey Brin"
some_dict['third'] = "Craig Silverstein"
some_dict['rstfi'] = "Vaibhav"

print(some_dict.arr)
del some_dict['second']
print("==============")
print(some_dict.arr)

