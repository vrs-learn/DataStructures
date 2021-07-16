# This program will implement the hash table with collision handlng
# This implementation talks using chaining. If there are more than one values for a particular hash, then the elements are saved as a list in 
# the particular hash.
# 
# Run this program and check further.
#


class HashTable:

    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX) ]

    def get_hash(self,key):
        h = 0 
        for elem in key:
            h += ord(elem)
        return h % self.MAX
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for index, elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][index] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][idx]
                break


new_dict = HashTable()
new_dict['first'] = "jason"
new_dict['second'] = "andrew"
new_dict['third'] = "karan"

print(new_dict.arr)
new_dict['second'] = "chin li"
new_dict['ondsec'] = "cpoar"
print(new_dict.arr)