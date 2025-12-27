class Dumela:
  def __init__(self):
    self.name=input('Enter name: ')

  def __str__(self):
    return f'Dumela {self.name}.'

print(Dumela())
