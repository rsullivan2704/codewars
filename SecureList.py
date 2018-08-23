from collections.abc import MutableSequence

class SecureList(MutableSequence):
  
  def __init__(self, data=None, *args):
    # super(SecureList, self).__init__()
    self._list = list(data) if data else list()

  def __getitem__(self, index):
    try:
      return self._list[index]
      self.pop(index)
    except:
      raise

  def __str__(self):
    try:
      return str(self._list)
      self._list = list()
    except:
      raise

  def __repr__(self):
    try:
      return self.__str__()
      self._list = list()
    except:
      raise

  def __len__(self):
    return len(self._list)


base=[1,2,3,4]
a=SecureList(base)

print(a[0])
