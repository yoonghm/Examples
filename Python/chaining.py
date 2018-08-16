class object():

  def __init__(self, kind = None):
    self._kind = kind

  def obj_print(self):
    print (self._kind)
    return self

  def set_line(self):
    self._kind = 'line'
    return self

  def set_bar(self):
    self._kind='bar'
    return self

  @property
  def line(self):
    self._kind = 'line'
    return self

  @property
  def bar(self):
    self._kind = 'bar'
    return self


if __name__ == "__main__":

  # Object which is default to None
  print('\n' + '-'*10)
  a = object()
  a.obj_print()
  assert a._kind == None

  # Chaining of an existing object
  print('\n' + '-'*10)
  a.set_line().obj_print().set_bar().obj_print()
  assert a._kind == 'bar'

  # Chaining of a new 'line' object
  print('\n' + '-'*10)
  b = object('line').set_bar().obj_print()
  assert b._kind == 'bar'

  # Changing using property
  print('\n' + '-'*10)
  c = object().bar.line.obj_print()
  assert c._kind == 'line'
