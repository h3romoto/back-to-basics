class HashTable:
  def __init__(self, size):
    self.max = size
    self.arr = [ [] for i in range(self.max)]

  def get_hash(self, key):
    hsh = 0 
    for char in key:
      # get ASCII value
      hsh += ord(char)
    return hsh%self.max
  
  def __setitem__(self, key, value):
    hsh = self.get_hash(key)
    for indx, element in enumerate(self.arr[hsh]):
      if len(element) == 2 & element[0] == key:
        self.arr[hsh][indx] = (key, value)
      else:
        self.arr[hsh].append((key, value))

  def __getitem__(self, key):
    hsh = self.get_hash(key)
    for element in self.arr[hash]:
      if element[0] == key:
        return element[1]
  
  def __deleteitem__(self, key):
    hsh = self.get_hash(key)
    for indx, element in enumerate(self.arr[hash]):
      if element[0] == key:
        del self.arr[hsh][indx]


tble = HashTable(5)
tble['day'] = 1
print(tble['day'])