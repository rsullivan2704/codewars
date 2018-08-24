from collections.abc import MutableSequence

class SecureList(MutableSequence):
  
  def __init__(self, data=None, *args):
    self._list = list(data) if data else list()

  def __getitem__(self, index):
    try:
      item = self._list[index]
      self._list.pop(index)
    except:
      raise
    return item

  def __str__(self):
    try:
      result = str(self._list)
      self._list = list()
    except:
      raise
    return result

  def __repr__(self):
    return self.__str__()

  def __len__(self):
    return len(self._list)

  def __delitem__(self, value):
    self._list.remove(value)

  def __setitem__(self, index, value):
    self._list.insert(index, value)

  def insert(self, index, value):
    self.__setitem__(index, value)


base=[1,2,3,4]
a=SecureList(base)
b=SecureList(None)

print(a[0])
print(a)

print(b)
