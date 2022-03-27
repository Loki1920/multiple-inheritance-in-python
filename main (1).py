# multiple inheritance in python
class Father:
  def __init__(self):
    super().__init__()
    print("father class constructor:")
  def showF(self):
    print("father class method:")
class Mother:
  def __init__(self):
    super().__init__()
    print("mother class constructor:")
  def showM(self):
    print("mother class method:")

class Son(Father,Mother):
  def __init__(self):
    super().__init__()
    print("son class constuctor:")
  def showS(self):
    print("son class method:")

s = Son()